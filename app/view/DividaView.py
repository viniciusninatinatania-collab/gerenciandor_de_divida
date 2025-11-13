
from datetime import datetime, date, timedelta

FORMATO_DATA = "%d/%m/%Y"

class DividaView:

    def listar_dividas(self, dividas):
        input()
           # Cabeçalho
        print("\n--- Lista de Dívidas ---")
        print("ID | NOME (Dívida)       | VALOR    | VENCIMENTO | STATUS")
        print("---|--------------------|----------|------------|---------")
        for divida in dividas:
            # Formatando o valor para duas casas decimais
            print(
                f"[{divida.id}] {divida.nome:20.20s} | R$ {divida.valor:8.2f} | Venc: {divida.data_vencimento or 'N/A'} | {divida.situacao}"
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
    def mostrar_relatorio(self, dados):
     print("\n=== RELATÓRIO GERAL DE DÍVIDAS ===")
     print(f"{'ID':<5} {'NOME':<15} {'VALOR (R$)':<12} {'STATUS':<10} {'VENCIMENTO':<12}")
     print("-" * 60)

     for d in dados["lista"]:
        print(f"{d['id']:<5} {d['nome']:<15} {d['valor']:<12.2f} {d['situacao']:<10} {d['data_vencimento'] or 'N/A':<12}")

     print("\n--- RESUMO ---")
     print(f"Total de Dívidas:  R$ {dados['total']:.2f}")
     print(f"Total Pagas:       R$ {dados['pago']:.2f}")
     print(f"Total Pendentes:   R$ {dados['pendente']:.2f}")
     print("-" * 40)
    def pedir_nome_arquivo(self):
        return input("Nome do arquivo CSV (ex: dividas.csv): ").strip()

    def mostrar_exportacao_sucesso(self, nome_arquivo):
        print(f"Exportado para {nome_arquivo} com sucesso.")

    def mostrar_exportacao_erro(self, mensagem):
        print(f"Erro ao exportar: {mensagem}")


        
