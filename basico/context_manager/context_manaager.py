import sqlite3 as sql
import numpy as np

with sql.connect("databse.db") as conn, open("dados.txt", 'r', encoding='utf8') as data:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
        )
    """)

    linhas = data.readlines()

    dtype = np.dtype([('nome', 'U30'),
                      ('email', 'U30'),])
    valores = np.empty((len(linhas)), dtype=dtype)

    for i, linha in enumerate(linhas):
        nome, email = linha.strip().split(',')
        valores[i] = (nome, email)

    cursor.executemany(
        "INSERT INTO funcionarios (nome, email) VALUES (?, ?)",
        valores.tolist()
    )

conn.close()