class DividaView:
    def listar_dividas(self, dividas):
        for divida in dividas:
            print(f"Dívida ID: {divida.id}, Valor: {divida.valor}, Vencimento: {divida.data_vencimento}, Status: {divida.situacao}")

    def mostrar_erro(self, mensagem):
        print(f"[ERRO] {mensagem}")