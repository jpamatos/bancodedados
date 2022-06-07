import b.inicial
import psycopg2

# Método para conectar o banco de dados
def conecta_db():
    con = psycopg2.connect(host = 'localhost',
                            database = 'bdviagens',
                            user = b.inicial.usuario,
                            password = b.inicial.senha)
    return con

# Método para criar uma tabela
def criar_db(sql):
    con = conecta_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

# Método para inserir múltiplos dados em uma tabela
def inserir_db(sql):
    con = conecta_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

# Método para realizar uma consulta generalizada
def consultar_db(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  recset = cur.fetchall()
  registros = []
  for rec in recset:
    registros.append(rec)
  con.close()
  return registros

# Método para inserir uma tupla
def insere_tupla(sql,tupla): 
    con = conecta_db()
    cur = con.cursor()
    try:
        cur.execute(sql,tupla)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

# Método para realizar alterações e buscas personalizadas
def buscaTupla(sql,tupla):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql,tupla)
  recset = cur.fetchall()
  registros = []
  for rec in recset:
    registros.append(rec)
  con.close()
  return registros
