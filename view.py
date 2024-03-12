import sqlite3 as lite

con = lite.connect('dados.db')

def inserir_form(i):
    with con: 
        cur = con.cursor()
        query = "INSERT INTO inventorio(lote, tipo, local, status, entrada, retirada, peso) VALUES(?,?,?,?,?,?,?)"
        cur.execute(query, i)

def atualizar_(i):
    with con: 
        cur = con.cursor()
        query = "UPDATE inventorio SET lote=?, tipo=?, local=?, status=?, entrada=?, retirada=?, peso=? WHERE id=?"
        cur.execute(query, i)

def deletar_form(i):
    with con: 
        cur = con.cursor()
        query = "DELETE FROM inventorio WHERE id=?"
        cur.execute(query, i)

def ver_form():
    ver_dados = []
    with con: 
        cur = con.cursor()
        query = "SELECT * FROM inventorio"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

def ver_item(id):
    ver_dados_individual = []
    with con: 
        cur = con.cursor()
        query = "SELECT * FROM inventorio WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)