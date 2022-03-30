import psycopg2 ##postgresql

params = {
  'dbname': '', 
  'user': '',
  'password': '',
  'host': '',
  'port': ''
}

# conn = psycopg2.connect(**params)

# print(type(conn))

def connect():
    return psycopg2.connect(**params)
