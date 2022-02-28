import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=HSN;'
                      'Database=Contech-DB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM ingredients')

for i in cursor:
    print(i)