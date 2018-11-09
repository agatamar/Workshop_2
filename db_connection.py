from psycopg2 import connect,OperationalError

def get_connection(base='workshop2'):
    username='postgres'
    haslo='coderslab'
    host='localhost'

    try:
        cnx=connect(host=host,user=username,password=haslo, database=base)
        return cnx
    except OperationalError:
        return None