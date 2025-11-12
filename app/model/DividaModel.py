from datetime import datetime, date, timedelta
from .db import get_connection

class DividaModel:
    def __init__(self, id, nome, valor, descricao, data_vencimento, situacao, criado_em):
        self.id = id;
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.situacao = situacao
        self.criado_em = criado_em

    @staticmethod
    def adicionar_divida( nome, valor, descricao, data_vencimento):
        try:
            # === Validações ===
            if not nome:
                raise ValueError("O nome é obrigatório.")
        
            valor = float(valor)

            if valor <= 0:
                raise ValueError("O valor deve ser maior que zero.")

            # === Atribuições ===
            nome = nome
            valor = valor
            descricao = descricao
            data_vencimento = data_vencimento
            criado_em = datetime.now().isoformat()

            # === Inserção no banco ===
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO dividas (nome, valor, data_vencimento, descricao, situacao, criado_em) VALUES (?, ?, ?, ?, 'pendente', ?)",
                (nome, valor, data_vencimento, descricao, criado_em)
            )

            conn.commit()

            return True
        except Exception as e:
           
            # Erros de validação (nome vazio, valor inválido)
           return f"Erro de validação: {e}"

        finally:
            # Sempre fecha a conexão mesmo se der erro
            try:
                conn.close()
            except:
                pass

    @staticmethod
    def get_dividas():
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dividas")
            rows = cursor.fetchall()
            dividas = []
            for row in rows:
                divida = DividaModel(
                    id=row["id"],
                    nome=row["nome"],
                    valor=row["valor"],
                    descricao=row["descricao"],
                    data_vencimento=row["data_vencimento"],
                    situacao=row["situacao"],
                    criado_em=row["criado_em"]
                )
                dividas.append(divida)
            return dividas
        except Exception as e:
            print(f"Erro ao buscar dívidas: {e}")
            return []
        finally:
            try:
                conn.close()
            except:
                pass
    
    @staticmethod
    def get_divida_por_id(divida_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dividas WHERE id = ?", (divida_id,))
            row = cursor.fetchone()
            if row:
                divida = DividaModel(
                    id=row["id"],
                    nome=row["nome"],
                    valor=row["valor"],
                    descricao=row["descricao"],
                    data_vencimento=row["data_vencimento"],
                    situacao=row["situacao"],
                    criado_em=row["criado_em"]
                )
                return divida
            return None
        except Exception as e:
            print(f"Erro ao buscar dívida por ID: {e}")
            return None
        finally:
            try:
                conn.close()
            except:
                pass

    @staticmethod
    def atualizar_situacao_divida(divida_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE dividas SET situacao = 'paga' WHERE id = ?",
                (divida_id,)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao marcar dívida como paga: {e}")
            return False
        finally:
            try:
                conn.close()
            except:
                pass
    
    @staticmethod
    def excluir_divida(divida_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM dividas WHERE id = ?", (divida_id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao excluir dívida: {e}")
            return False
        finally:
            try:
                conn.close()
            except:
                pass
    @staticmethod
    def editar_divida(divida_id, nome=None, valor=None, descricao=None, data_vencimento=None, situacao=None):
       try:
           conn = get_connection()
           cursor = conn.cursor()
           cursor.execute('SELECT * FROM dividas WHERE id = ?', (divida_id,))
           row = cursor.fetchone()

           if not row:
               return f'Dívida com ID {divida_id} não encontrada.'
           novo_nome = nome if nome is not None else row['nome']
           novo_valor = valor if valor is not None else row['valor']
           nova_descricao = descricao if descricao is not None else row['descricao']
           nova_data_vencimento = data_vencimento if data_vencimento is not None else row['data_vencimento']
           nova_situacao = situacao if situacao is not None else row['situacao']


           #validação do valor
           try:
               novo_valor = float(novo_valor)
               if novo_valor <= 0:
                   raise ValueError('O valor deve ser maior que zero.')
           except ValueError as e:
               return f'Valor inválido: {e}'
           
           #atualizar a divida no banco
           cursor.execute("""
            UPDATE dividas
            SET nome = ?, valor = ?, descricao = ?, data_vencimento = ?, situacao = ?
            WHERE id = ?
        """, (novo_nome, novo_valor, nova_descricao, nova_data_vencimento, nova_situacao, divida_id))
           conn.commit()

           return True
       except Exception as e:
        return f'Erro ao editiar dívida: {e}'
       finally:
        try:
            conn.close()
       
        except:
            pass
    @staticmethod
    def gerar_relatorio():
        try:
         conn = get_connection()
         cursor = conn.cursor()

        #busca todas as dívidas do banco
         cursor.execute("SELECT nome, valor, descricao, data_vencimento, situacao FROM dividas")
         dividas = cursor.fetchall()

         if not dividas:
            print("\n Nenhuma dívida registrada.")
            return

         total_dividas = sum(float(d['valor']) for d in dividas)
         total_pendente = sum(float(d['valor']) for d in dividas if d['situacao'].lower() == 'pendente')
         dividas_pendentes = [d for d in dividas if d['situacao'].lower() == 'pendente']

         print("\n========== RELATÓRIO DE DÍVIDAS ==========")
         print(f" Total de Dívidas Registradas: R$ {total_dividas:.2f}")
         print(f" Total Pendente a Pagar: R$ {total_pendente:.2f}")
         dividas_pendentes = [d for d in dividas if d['situacao'].lower() == 'pendente']
         dividas_pagas = [d for d in dividas if d['situacao'].lower() == 'paga']

         print("\n Dívidas Pendentes:")
         if not dividas_pendentes:
            print("Nenhuma dívida pendente encontrada.")
         else:
             for d in dividas_pendentes:
                print(f"- {d['nome']} | {d['descricao']} | R$ {d['valor']:.2f} | Vencimento: {d['data_vencimento']}")

         print("===========================================\n")
         print("\n Dívidas Pagas:")
         if not dividas_pagas:
            print("Nenhuma dívida paga encontrada.")
         else:
            for d in dividas_pagas:
                print(f"- {d['nome']} | {d['descricao']} | R$ {d['valor']:.2f} | Vencimento: {d['data_vencimento']}")

         print("===========================================\n")    
        except Exception as e:
            print(f'Erro ao gerar relatório: {e}')
        
        finally:
            try:
                conn.close()
            except:
                pass
        





