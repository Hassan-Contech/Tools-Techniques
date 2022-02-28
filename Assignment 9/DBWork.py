import re
import pyodbc
from essential_generators import DocumentGenerator

ServerName = 'HSN'
DatabaseName = 'ContechDB'
TableName = 'Assignment9'


def GetRandomWords():
    gen = DocumentGenerator()
    return gen.sentence()

def CreateDatabase():
    try:
        conn = pyodbc.connect("Driver={SQL Server};Server=" + ServerName +";Trusted_Connection=yes;")
        print('Connected to SQL Server Successfully')
    except:
        print('Connection failed to SQL Server')

    cursor = conn.cursor()
    conn.autocommit = True

    # Check if the database already exists.
    cursor.execute("SELECT name FROM master.dbo.sysdatabases where name=?;",(DatabaseName,))
    data=cursor.fetchall()

    #Printing if database exists or not
    if not data:
        cursor.execute("CREATE DATABASE ContechDB;")
        print("'{}' Database has been created.".format(DatabaseName))
    else:
        print("'{}' Database already exists".format(DatabaseName))
    

def CreateTable():
    conn = pyodbc.connect("Driver={SQL Server};Server=" + ServerName + ";Database=" + DatabaseName +";Trusted_Connection=yes;")
    cursor = conn.cursor()
    conn.autocommit = True
    cursor.execute("IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='" + TableName + "' AND xtype='U') CREATE TABLE " + TableName + "(Id INT, EnglishWord VARCHAR(250))")  
    conn.commit()
    
def InsertData():
    counter = 1
    totalRecord = 20 #1000000
    conn = pyodbc.connect("Driver={SQL Server};Server=" + ServerName + ";Database=" + DatabaseName +";Trusted_Connection=yes;")
    cursor = conn.cursor()
    conn.autocommit = True
    while counter <= totalRecord:
        cursor.execute("INSERT INTO " + TableName + " (Id,EnglishWord) values(?,?)", counter, GetRandomWords())
        counter = counter + 1
    cursor.close()

def GetFirstRecord():
    conn = pyodbc.connect("Driver={SQL Server};Server=" + ServerName + ";Database=" + DatabaseName +";Trusted_Connection=yes;")
    cursor = conn.cursor()
    conn.autocommit = True
    for row in cursor.execute("SELECT TOP 1 EnglishWord FROM " + TableName):
        return row

def FindLongestWord(sentence):
    longest = max(sentence.split(), key=len)
    print("First record: " + sentence)
    print("Longest word is: ", longest)
    print("Length Longest word is: ", len(longest))
    if(len([m.start() for m in re.finditer(longest, sentence)]) > 1):
        print("Number of occurrences for '" + longest +"': ", len([m.start() for m in re.finditer(longest, sentence)]))



CreateDatabase()
CreateTable()
InsertData()
res = GetFirstRecord()
FindLongestWord(res[0])

