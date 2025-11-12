from datetime import datetime, date, timedelta

FORMATO_DATA = "%d/%m/%Y"

class DividaView:

    def listar_dividas(self, dividas):
        input()
        for divida in dividas:
           print(
                f"Dívida ID: {divida.id}, Valor: {divida.valor}, "
                f"Vencimento: {self.ler_data(divida.data_vencimento)}, "
                f"Status: {divida.situacao}"
            )
           
    def mostrar_detalhes_divida(self, divida):
        input()
        print(
            f"Detalhes da Dívida ID: {divida.id}, Nome: {divida.nome}, Valor: {divida.valor}, Data de Vencimento: {self.ler_data(divida.data_vencimento)}, Descrição: {divida.descricao}, Criado em: {self.ler_data(divida.criado_em)}"
        )
       
    def mostrar_erro(self, mensagem):
        input()
        print(f"[ERRO] {mensagem}")

    def mostrar_sucesso(self, mensagem):
        input()
        print(mensagem)


    def ler_data(self, texto):
        if not texto:
            return ""
        try:
            data = datetime.strptime(texto, "%Y-%m-%d").date()
            return data.strftime("%d/%m/%Y")
        except:
            return ""
        