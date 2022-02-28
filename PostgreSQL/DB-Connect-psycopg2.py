import psycopg2
import sys

con = None
databaseName = 'Contech-DB'
try:
    con = psycopg2.connect(database=databaseName, user='postgres', password='somePassword')
    cur = con.cursor()
    cur.execute('SELECT version()')

    version = cur.fetchone()[0]
    print(version)
    
    cur.execute("""SELECT datname from pg_database""")
    rows = cur.fetchall()
    print("\nShow me the databases:\n")
    for row in rows:
        print ("   ", row[0])
        
except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:

    if con:
        print('Connected to DB: ' + databaseName)
        con.close()