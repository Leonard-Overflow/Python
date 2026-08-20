import sqlite3 as sql
import numpy as np

with sql.connect("databse.db") as conn, open("dados.txt", 'r', encoding='utf8') as data:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE funcionarios(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
        )
    """)
    dtype = np.dtype([('nome', 'U30'),
                      ('email', 'U30'),])

    valores = np.empty((1, 2), dtype=dtype)

    for linha in data:
        lista = np.array(linha.split(','))