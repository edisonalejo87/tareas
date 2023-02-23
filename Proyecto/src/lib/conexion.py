import psycopg2
def conecion():
# Connect to your postgres DB
    try:
        conn = psycopg2.connect(
            user='postgres',
            password='postgres',
            host='127.0.0.1',
            database='proyecto',
        )
        print("me conecte")
    except Exception as err:
        print(f'error no pudiste conectarte"{err}')
    return conn
# Open a cursor to perform database operations
cur = conecion(). cursor()

# Execute a query
cur.execute("SELECT * FROM roles")

# Retrieve query results
records = cur.fetchall()
print(records)