database.py

import sqlite3

# Criar conexão com banco de dados SQLite
conn = sqlite3.connect("care_assistant.db")
cursor = conn.cursor()

# Criar tabela para lembretes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS lembretes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        horario TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
