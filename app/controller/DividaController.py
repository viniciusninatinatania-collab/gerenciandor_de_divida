from ..model.DividaModel import DividaModel
from ..view.DividaView  import DividaView
from datetime import datetime, date, timedelta
import csv

class DividaController:
    def __init__(self):
        self.view = DividaView()

    def adicionar_divida(self, nome, valor, descricao, data_vencimento):
       try:

        resultado = DividaModel.adicionar_divida( nome, valor, descricao, data_vencimento)

        if resultado is True:
           self.view.mostrar_sucesso(f"Dívida '{nome}' adicionada com sucesso.")
        
       except Exception as e:
        self.view.mostrar_erro(f"Erro inesperado ao adicionar dívida: {e}")

    def lista_todas_dividas(self):
        dividas = DividaModel.get_dividas()
        if not dividas:
            self.view.mostrar_erro("Nenhuma dívida encontrada.")
            return 
        else:
            self.view.listar_dividas(dividas)

    def listar_dividas_pendentes(self):
        dividas = DividaModel.get_dividas()
        if not dividas:
            self.view.mostrar_erro("Nenhuma dívida encontrada.")
            return 
        else:
            dividas_pendentes = [d for d in dividas if d.situacao == 'pendente']
            self.view.listar_dividas(dividas_pendentes)

    def listar_dividas_pagas(self):
        dividas = DividaModel.get_dividas();
        if not dividas:
            self.view.mostrar_erro("Nenhuma dívida encontrada.")
            return
        else:
            dividas_pagas = [d for d in dividas if d.situacao == 'paga']
            self.view.listar_dividas(dividas_pagas)
    
    def mostrar_detalhes_divida(self, divida_id):
        divida_id = int(divida_id)
        divida = DividaModel.get_divida_por_id(divida_id)
        if not divida:
            self.view.mostrar_erro(f"Dívida com ID {divida_id} não encontrada.")
            return
        else:
            self.view.mostrar_detalhes_divida(divida)

    def atualizar_situacao_divida(self, divida_id):
        divida_id = int(divida_id)

        divida = DividaModel.get_divida_por_id(divida_id)
        if not divida:
            self.view.mostrar_erro(f"Dívida com ID {divida_id} não encontrada.")
            return
        if divida.situacao == 'paga':
            self.view.mostrar_erro(f"A dívida com ID {divida_id} já está marcada como paga.")
            return
        sucesso = DividaModel.atualizar_situacao_divida(divida_id)
        if sucesso:
            self.view.mostrar_sucesso(f"Dívida com ID {divida_id} marcada como paga com sucesso.")
        else:
            self.view.mostrar_erro(f"Erro ao marcar a dívida com ID {divida_id} como paga.")\
            
    def excluir_divida(self, divida_id):
        divida_id = int(divida_id)

        divida = DividaModel.get_divida_por_id(divida_id)
        if not divida:
            self.view.mostrar_erro(f"Dívida com ID {divida_id} não encontrada.")
            return
        sucesso = DividaModel.excluir_divida(divida_id)
        if sucesso:
            self.view.mostrar_sucesso(f"Dívida com ID {divida_id} excluída com sucesso.")
        else:
            self.view.mostrar_erro(f"Erro ao excluir a dívida com ID {divida_id}.")
    def editar_divida(self, divida_id):
        divida_id = int(divida_id)

        #solicitar novo valor
        divida = DividaModel.get_divida_por_id(divida_id)
        if not divida:
            self.view.mostrar_erro(f'Divida com ID {divida_id} não encontrada.')
            return
        novo_nome = input(f"Novo nome ({divida.nome}): ") or None
        novo_valor = input(f"Novo valor ({divida.valor}): ") or None
        nova_descricao = input(f"Nova descrição ({divida.descricao}): ") or None
        nova_data_vencimento = input(f"Nova data de vencimento ({divida.data_vencimento}): ") or None
        novo_status = input(f"Novo status ({divida.situacao}) [pendente/paga]: ") or None


        resultado = DividaModel.editar_divida(divida_id, novo_nome, novo_valor, nova_descricao, nova_data_vencimento, situacao=novo_status)

        if resultado is True:
            self.view.mostrar_sucesso(f"Divida ID {divida_id} atualizada com sucesso.")
        else:
            self.view.mostrar_erro(resultado)

    def relatorio(self):
        DividaModel.gerar_relatorio()
    def exportar_dividas_csv(self):
        nome_arquivo = self.view.pedir_nome_arquivo()
        if not nome_arquivo:
            self.view.mostrar_exportacao_erro("Nome inválido.")
            return

        dividas = DividaModel.get_dividas()
        if not dividas:
            self.view.mostrar_exportacao_erro("Nenhuma dívida para exportar.")
            return

        try:
            with open(nome_arquivo, "w", newline='', encoding="utf-8") as f:
                escritor = csv.writer(f)
                escritor.writerow(["id", "nome", "valor", "data_vencimento", "descricao", "situacao", "criado_em"])
                for d in dividas:
                    escritor.writerow([
                        d.id, d.nome, d.valor,
                        d.data_vencimento, d.descricao,
                        d.situacao, d.criado_em
                    ])
            self.view.mostrar_exportacao_sucesso(nome_arquivo)
        except Exception as e:
            self.view.mostrar_exportacao_erro(str(e))
    def dividas_vencendo_proximos_7_dias(self):
     dividas = DividaModel.get_dividas()
     if not dividas:
         self.view.mostrar_erro("Nenhuma dívida encontrada.")
         return

     hoje = datetime.now().date()
     sete_dias = hoje + timedelta(days=7)
     proximas = []

     for d in dividas:
        if d.data_vencimento:
            try:
                vencimento = datetime.strptime(d.data_vencimento, "%Y-%m-%d").date()
                if hoje <= vencimento <= sete_dias:
                    proximas.append(d)
            except:
                pass

    # Verifica após o loop, não dentro dele
     if not proximas:
        self.view.mostrar_erro("Nenhuma dívida com vencimento nos próximos 7 dias.")
     else:
        self.view.listar_dividas(proximas)
    
    def buscar_divida(self):
        termo = input("Buscar por nome ou descrição: ").strip()

        if not termo:
            self.view.mostrar_erro("Nada informado.")
            return

        resultados = DividaModel.buscar_por_termo(termo)

        if not resultados:
            self.view.mostrar_erro("Nenhuma dívida encontrada com esse termo.")
            return

        self.view.listar_dividas(resultados)