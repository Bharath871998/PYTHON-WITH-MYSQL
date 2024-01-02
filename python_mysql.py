'''
PYTHON MYSQL DATABASE TUTS

import mysql.connector

# To create connection to database using username and password
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Avik@2021',
)
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Avik@2021',
    database = 'python_snake'
)

print(mydb)

# Initializing the cursor
mycursor = mydb.cursor()

# To create database
mycursor.execute("CREATE DATABASE python_snake")

# To see the existing database
mycursor.execute("SHOW DATABASES")

# To create table
mycursor.execute("CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), tech VARCHAR(255))")
print("Table created successfully")

# To see the created tables
mycursor.execute("SHOW TABLES")
for db in mycursor:
     print(db)

# To add the records into the table
col = "INSERT INTO employees (name, tech) VALUES (%s, %s)"
val = [
    ('Bharath KK', 'Python'),
    ('Rajkumar', 'Maya app'),
    ('Sameer', 'Java')
]
mycursor.executemany(col, val)
mydb.commit()
print(mycursor.rowcount, 'was inserted in employees table')

# To see all the records in the table
mycursor.execute("SELECT * FROM employees")
res = mycursor.fetchall()
print(res)

# To see only one record from the table
res = mycursor.fetchone()
print(res)

# To delete all records from the table 
mycursor.execute("TRUNCATE TABLE employees")
print("ALL DELETED")

# To drop table from the database
mycursor.execute("DROP TABLE employees")
print("Table deleted")

# To drop the database
mycursor.execute("DROP DATABASE python_snake")
print("Database deleted")
'''