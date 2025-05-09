import sqlite3
import json
import os

DB_PATH = "dados_embrapa.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dados_embrapa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            ano INTEGER NOT NULL,
            dados_json TEXT NOT NULL,
            UNIQUE(categoria, ano)
        );
    """)
    conn.commit()
    conn.close()

def salvar_dados_no_banco(categoria, ano, dados):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    dados_json = json.dumps(dados, ensure_ascii=False)
    cursor.execute("""
        INSERT OR REPLACE INTO dados_embrapa (categoria, ano, dados_json)
        VALUES (?, ?, ?)
    """, (categoria, ano, dados_json))
    conn.commit()
    conn.close()

def buscar_dados_do_banco(categoria, ano):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT dados_json FROM dados_embrapa
        WHERE categoria = ? AND ano = ?
    """, (categoria, ano))
    row = cursor.fetchone()
    conn.close()
    return json.loads(row[0]) if row else None