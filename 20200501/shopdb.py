import sqlite3
conn = sqlite3.connect('myshop.db')

def create_lable():
  c = conn.cursor()
  sql = """
     CREATE TABLE products (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      price REAL NOT NULL,
      desc TEXT NOT NULL,
      image TEXT NOT NULL
     )
  """
  c.execute(sql)

  conn.commit()
  conn.close()
create_table()

def insert_product(conn, name, price, desc, img):
  c = conn.cursor()
  sql = """

  """
  c.execute(sql, (name, price, desc, img))
  conn.commit()

def select_products(conn):
  c = conn.cursor()
  sql = ''
  c.execute(sql)
  return c. fetchall()

def select_by_id(conn, sid ):
  c = conn.cursor()
  sql = '' + str(sid)
  c.execute(sql)
  return c. fetchall()
  
print(select_by_id(conn, 1))

def update_product(conn, id, name, price, desc, img):
  sql

  
