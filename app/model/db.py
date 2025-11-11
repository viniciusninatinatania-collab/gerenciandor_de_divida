import sqlite3
import os


# Caminho absoluto baseado no LOCAL do arquivo db.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "dividas.db")


def get_connection():
    """"Retorna uma conexão com o banco."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dividas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            valor REAL NOT NULL,
            data_vencimento TEXT,
            descricao TEXT,
            situacao TEXT NOT NULL DEFAULT 'pendente',
            criado_em TEXT NOT NULL
        )
    """)
    con.commit()
    con.close()
