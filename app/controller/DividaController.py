from ..model.DividaModel import DividaModel
from ..view.DividaView  import DividaView

class DividaController:
    def __init__(self):
        self.view = DividaView()

    def adicionar_divida(self, nome, valor, descricao, data_vencimento):
       try:

        resultado = DividaModel.adicionar_divida( nome, valor, descricao, data_vencimento)

        if resultado is True:
           self.atualizar_lista_dividas()
        
       except Exception as e:
        self.view.mostrar_erro(f"Erro inesperado ao adicionar dívida: {e}")

    def atualizar_lista_dividas(self):
        dividas = DividaModel.get_dividas()
        if not dividas:
            self.view.mostrar_erro("Nenhuma dívida encontrada.")
            return 
        else:
            self.view.listar_dividas(dividas)

        
