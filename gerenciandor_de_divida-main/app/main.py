
from datetime import datetime, date, timedelta
import os
import csv

from .controller.DividaController import DividaController

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    controller = DividaController()
 
    print("=== Sistema de Gerenciamento de Dívidas ===")

    while True:
        print("\n1. Adicionar dívida")#funcionando
        print("2. Listar todas as dívidas")#funcionando
        print("3. Listar dívidas pendentes")#funcionando
        print("4. Listar dívidas pagas")#funcionando
        print("5. Mostrar detalhes da dívida(ID)")#funcionando
        print("6. Marcar dívida como paga (ID)")#funcionando
        print("7. Editar dívida (ID)")#funcionando
        print("8. Excluir divida (ID)")#funcionando
        print("9. Buscar")#funcionando
        print("10. Relatório")#funcionando
        print("11. Exportar CSV")#funcionando
        print("12. Vencimentos próximos (7 dias)")#funcionando
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            valor = input("Valor: ")
            descricao = input("Descrição: ")
            data_vencimento = input("Data de vencimento (YYYY-MM-DD): ")
            controller.adicionar_divida(nome, valor, descricao, data_vencimento)

        elif opcao == "2":
            controller.lista_todas_dividas()

        elif opcao == "3":
            controller.listar_dividas_pendentes()

        elif opcao == "4":
            controller.listar_dividas_pagas()
        
        elif opcao == "5":
            id_divida = input("ID da dívida: ")
            controller.mostrar_detalhes_divida(id_divida)
        
        elif opcao == "6":
            id_divida = input("ID da dívida: ")
            controller.atualizar_situacao_divida(id_divida)
            
        elif opcao == "7":
            id_divida = input("ID da dívida: ")
            controller.editar_divida(id_divida)

        elif opcao == "8":
            id_divida = input("ID da dívida: ")
            controller.excluir_divida(id_divida)
        elif opcao == '10':
            controller.relatorio()  
        elif opcao == '11':
            controller.exportar_dividas_csv()
        elif opcao == "12":
            controller.dividas_vencendo_proximos_7_dias()


        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

        input("\nPressione Enter para continuar...")
        limpar_tela()



FORMATO_DATA = "%d/%m/%Y"

if __name__ == "__main__":
   main()


# menu
# def menu_principal():
#     while True:
#         print("""
# ===== GERENCIADOR DE DÍVIDAS =====

# ==================================
# """)
#         opcao = input("Escolha: ").strip()
#         if opcao == '1':
#             adicionar_divida()
#         elif opcao == '2':
#             listar_dividas()
#         elif opcao == '3':
#             listar_dividas('pendente')
#         elif opcao == '4':
#             listar_dividas('paga')
#         elif opcao == '5':
#             i = entrada_id("ID da dívida: ")
#             if i: mostrar_detalhes(i)
#         elif opcao == '6':
#             i = entrada_id("ID da dívida: ")
#             if i: marcar_como_paga(i)
#         elif opcao == '7':
#             i = entrada_id("ID da dívida: ")
#             if i: editar_divida(i)
#         elif opcao == '8':
#             i = entrada_id("ID da dívida: ")
#             if i: excluir_divida(i)
#         elif opcao == '9':
#             buscar()
#         elif opcao == '10':
#             relatorio()
#         elif opcao == '11':
#             exportar_csv()
#         elif opcao == '12':
#             vencimentos_proximos(7)
#         elif opcao == '0':
#             print("Até logo!")
#             break
#         else:
#             print("Opção inválida.")

#         input("\nPressione Enter para continuar...")
#         limpar_tela()



# def solicitar_data(texto):
#     while True:
#         resposta = input(f"{texto} (AAAA-MM-DD) [vazio para nenhum]: ").strip()
#         if resposta == "":
#             return None
#         d = ler_data(resposta)
#         if d:
#             return d
#         print("Data inválida.")


# def entrada_id(prompt):
#     s = input(prompt).strip()
#     if not s.isdigit():
#         print("ID inválido.")
#         return None
#     return int(s)




# def exibir_linha(reg):
#     venc = reg["data_vencimento"] or "-"
#     return f"[{reg['id']:>3}] {reg['nome'][:35]:35} | R$ {reg['valor']:10.2f} | Venc: {venc:10} | {reg['situacao']:8}"


# # Operações principais



# def listar_dividas(filtro=None):
#     conexao = abrir_conexao()
#     cursor = conexao.cursor()

#     if filtro == "pendente":
#         cursor.execute("SELECT * FROM dividas WHERE situacao='pendente' ORDER BY data_vencimento IS NULL, data_vencimento")
#     elif filtro == "paga":
#         cursor.execute("SELECT * FROM dividas WHERE situacao='paga' ORDER BY criado_em DESC")
#     else:
#         cursor.execute("SELECT * FROM dividas ORDER BY situacao, data_vencimento IS NULL, data_vencimento")

#     registros = cursor.fetchall()
#     conexao.close()

#     if not registros:
#         print("Nenhuma dívida encontrada.")
#         return

#     for r in registros:
#         print(exibir_linha(r))


# def mostrar_detalhes(id_divida):
#     conexao = abrir_conexao()
#     cursor = conexao.cursor()
#     cursor.execute("SELECT * FROM dividas WHERE id=?", (id_divida,))
#     r = cursor.fetchone()
#     conexao.close()

#     if not r:
#         print("Dívida não encontrada.")
#         return

#     print("---- DETALHES ----")
#     print(f"ID: {r['id']}")
#     print(f"Nome: {r['nome']}")
#     print(f"Valor: R$ {r['valor']:.2f}")
#     print(f"Vencimento: {r['data_vencimento'] or '-'}")
#     print(f"Situação: {r['situacao']}")
#     print(f"Descrição: {r['descricao'] or '-'}")
#     print(f"Criado em: {r['criado_em']}")
#     print("-------------------")


# def marcar_como_paga(id_divida):
#     conexao = abrir_conexao()
#     cursor = conexao.cursor()

#     cursor.execute("SELECT situacao FROM dividas WHERE id=?", (id_divida,))
#     r = cursor.fetchone()

#     if not r:
#         print("Dívida não encontrada.")
#         conexao.close()
#         return

#     if r["situacao"] == "paga":
#         print("Essa dívida já está paga.")
#         conexao.close()
#         return

#     cursor.execute("UPDATE dividas SET situacao='paga' WHERE id=?", (id_divida,))
#     conexao.commit()
#     conexao.close()

#     print("Dívida marcada como paga.")


# def excluir_divida(id_divida):
#     conexao = abrir_conexao()
#     cursor = conexao.cursor()
#     cursor.execute("SELECT id, nome FROM dividas WHERE id=?", (id_divida,))
#     r = cursor.fetchone()

#     if not r:
#         print("Dívida não encontrada.")
#         conexao.close()
#         return

#     confirm = input(f"Tem certeza que deseja excluir [{r['id']}] {r['nome']}? (s/n): ").strip().lower()
#     if confirm == "s":
#         cursor.execute("DELETE FROM dividas WHERE id=?", (id_divida,))
#         conexao.commit()
#         print("Dívida removida.")
#     else:
#         print("Cancelado.")

#     conexao.close()


# def editar_divida(id_divida):
#     conexao = abrir_conexao()
#     cursor = conexao.cursor()
#     cursor.execute("SELECT * FROM dividas WHERE id=?", (id_divida,))
#     r = cursor.fetchone()

#     if not r:
#         print("Dívida não encontrada.")
#         conexao.close()
#         return

#     print("Deixe vazio para manter o atual.")

#     nome = input(f"Nome [{r['nome']}]: ").strip() or r['nome']

#     while True:
#         entrada = input(f"Valor [{r['valor']:.2f}]: ").strip()
#         if entrada == "":
#             valor = r['valor']
#             break
#         try:
#             valor = float(entrada.replace(",", "."))
#             break
#         except:
#             print("Valor inválido.")

#     entrada_venc = input(f"Vencimento [{r['data_vencimento'] or 'nenhum'}]: ").strip()
#     if entrada_venc == "":
#         venc = None
#     else:
#         venc = ler_data(entrada_venc)
#         if not venc:
#             print("Data inválida.")
#             conexao.close()
#             return

#     descricao = input(f"Descrição [{r['descricao'] or '-'}]: ").strip() or r['descricao']

#     situacao = input(f"Situação [{r['situacao']}] (pendente/paga): ").strip().lower()
#     if situacao not in ("pendente", "paga", ""):
#         print("Situação inválida.")
#         conexao.close()
#         return
#     situacao = situacao or r['situacao']

#     cursor.execute(
#         "UPDATE dividas SET nome=?, valor=?, data_vencimento=?, descricao=?, situacao=? WHERE id=?",
#         (nome, valor, venc.isoformat() if venc else None, descricao, situacao, id_divida)
#     )
#     conexao.commit()
#     conexao.close()

#     print("Dívida atualizada.")



# #Relatório e busca
# def relatorio():
#     conexao = abrir_conexao()
#     cursor = conexao.cursor()

#     cursor.execute("SELECT SUM(valor) FROM dividas")
#     total = cursor.fetchone()[0] or 0

#     cursor.execute("SELECT SUM(valor) FROM dividas WHERE situacao='pendente'")
#     total_pendente = cursor.fetchone()[0] or 0

#     cursor.execute("SELECT SUM(valor) FROM dividas WHERE situacao='paga'")
#     total_pago = cursor.fetchone()[0] or 0

#     cursor.execute("SELECT * FROM dividas WHERE situacao='pendente' AND data_vencimento IS NOT NULL ORDER BY data_vencimento LIMIT 1")
#     prox = cursor.fetchone()

#     conexao.close()

#     print("----- RELATÓRIO -----")
#     print(f"Total Geral: R$ {total:.2f}")
#     print(f"Total Pendente: R$ {total_pendente:.2f}")
#     print(f"Total Pago: R$ {total_pago:.2f}")

#     if prox:
#         print(f"Próxima dívida: [{prox['id']}] {prox['nome']} em {prox['data_vencimento']} - R$ {prox['valor']:.2f}")
#     else:
#         print("Próxima dívida: nenhuma")


# def buscar():
#     termo = input("Buscar por nome ou descrição: ").strip()
#     if not termo:
#         print("Nada informado.")
#         return

#     like = f"%{termo}%"

#     conexao = abrir_conexao()
#     cursor = conexao.cursor()
#     cursor.execute(
#         "SELECT * FROM dividas WHERE nome LIKE ? OR descricao LIKE ? ORDER BY data_vencimento", (like, like)
#     )
#     registros = cursor.fetchall()
#     conexao.close()

#     if not registros:
#         print("Nenhum resultado.")
#         return

#     for r in registros:
#         print(exibir_linha(r))


# def exportar_csv():
#     nome_arquivo = input("Nome do arquivo CSV (ex: dividas.csv): ").strip()
#     if not nome_arquivo:
#         print("Nome inválido.")
#         return

#     conexao = abrir_conexao()
#     cursor = conexao.cursor()
#     cursor.execute("SELECT * FROM dividas ORDER BY id")
#     registros = cursor.fetchall()
#     conexao.close()

#     try:
#         with open(nome_arquivo, "w", newline='', encoding="utf-8") as f:
#             escritor = csv.writer(f)
#             escritor.writerow(["id", "nome", "valor", "data_vencimento", "descricao", "situacao", "criado_em"])
#             for r in registros:
#                 escritor.writerow([r["id"], r["nome"], r["valor"], r["data_vencimento"], r["descricao"], r["situacao"], r["criado_em"]])
#         print(f"Exportado para {nome_arquivo}.")
#     except Exception as e:
#         print("Erro ao exportar:", e)


# def vencimentos_proximos(dias=7):
#     hoje = date.today()
#     fim = hoje + timedelta(days=dias)
#     conexao = abrir_conexao()
#     cursor = conexao.cursor()
#     cursor.execute(
#         "SELECT * FROM dividas WHERE situacao='pendente' AND data_vencimento IS NOT NULL AND data_vencimento BETWEEN ? AND ? ORDER BY data_vencimento",
#         (hoje.isoformat(), fim.isoformat())
#     )
#     registros = cursor.fetchall()
#     conexao.close()

#     if not registros:
#         print(f"Nenhuma dívida nos próximos {dias} dias.")
#         return

#     print(f"Dívidas nos próximos {dias} dias:")
#     for r in registros:
#         print(exibir_linha(r))



# # bloco principal
# if __name__ == "__main__":
#     try:
#         menu_principal()
#     except KeyboardInterrupt:
#         print("\nSaindo...")
