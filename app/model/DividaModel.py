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

