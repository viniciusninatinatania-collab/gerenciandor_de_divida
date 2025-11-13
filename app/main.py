
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
        elif opcao == '9':
            controller.buscar_divida()

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


