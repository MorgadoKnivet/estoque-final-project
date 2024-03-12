import sqlite3 as lite

con = lite.connect('dados.db')

with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventorio(id INTEGER PRIMARY KEY AUTOINCREMENT, lote DECIMAL, tipo TEXT, local TEXT, status TEXT, entrada DATE, retirada DATE, peso DECIMAL )")