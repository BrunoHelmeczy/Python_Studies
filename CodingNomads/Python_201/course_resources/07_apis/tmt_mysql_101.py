# 1) py -m pip install mysql-connector-python
import mysql.connector
from pathlib import Path

def getDBlogin():
    txt = Path().resolve().joinpath('CodingNomads/Python_201/course_resources/07_apis/secrets.txt')

    with txt.open('r') as Input:
        text = Input.read()
        secrets = {l.split('=')[0]: l.split('=')[1] for l in text.split('\n')}
    return secrets

def connect2DB(db_name = 'sakila'):
    loginDetails = getDBlogin()

    db = mysql.connector.connect(
        host = 'localhost',
        user = loginDetails['username'],
        passwd = loginDetails['password'],
        database = db_name
    )

    return db

def queryDB(query, db_object = connect2DB()):
    cursor = db_object.cursor()
    cursor.execute(query)

    cols = cursor.column_names
    res =  cursor.fetchall()

    res.insert(0, cols)
    return res

db = connect2DB()

queryDB("SELECT * FROM actor LIMIT 5", db_object = db)

# query = query_str
query_str = """
    SELECT 
            *
        FROM film_actor fa
        LEFT JOIN actor a USING(actor_id)
        LEFT JOIN film f USING(film_id)
    LIMIT 10
"""

res = queryDB(query_str, db_object=db)

# Create / Alter / Insert into Table
def alterDB(query, db_object = connect2DB()):
    cursor = db_object.cursor()
    cursor.execute(query)

    db_object.commit()

# CREATE TABLE
query = """
    CREATE TABLE test (
        name VARCHAR(16) NOT NULL, 
        created_at DATETIME NOT NULL, 
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT
    )
"""

# alterDB(query, db_object)

# DROP TABLE IF EXISTS
# alterDB('DROP TABLE IF EXISTS test', db_object)

# chk = queryDB("SELECT * FROM INFORMATION_SCHEMA.TABLES", db_object = db_object)
# chk[0]
# [t[2] for t in chk]

alterDB("""
    CREATE TABLE IF NOT EXISTS newTable (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        salary FLOAT(2) DEFAULT 100,
        active BOOLEAN DEFAULT true 
    )
""", db_object)

# INSERT INTO newTable (col1, col2, ...) VALUES (val1, val2, ...), (val1, val2, ...)
alterDB("""
    INSERT INTO newTable (name, salary, active) VALUES
        ('record1', 80000, false),
        ('record2', 70000, true)
""", db_object)

# queryDB("SELECT * FROM newTable", db_object) # check yourself




