import mysql.connector
#connect to the database server
try:
    conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Soni1dec@",
    database="flights"
    )
    mycursor = conn.cursor()
    print("Connected to MySQL")
except:
    print("Error connecting to MySQL")
#create a database on the db server
#mycursor.execute("CREATE DATABASE flights")
#conn.commit()

#create a table
# airport -> airport_id | code | name|city
#mycursor.execute("""
#CREATE TABLE airport(
    #airport_id INTEGER PRIMARY KEY ,
    #code VARCHAR(10) NOT NULL,
    #city VARCHAR(50) NOT NULL,
    #name VARCHAR(50) NOT NULL
#)
#""")
#conn.commit()

#Insert data to the table
#mycursor.execute("""
    #INSERT INTO airport VALUES
    #(1,'DEL','New Delhi','IGIA'),
    #(2,'CCU','KOLKATA','NSCA'),
    #(3,'BOM','MUMBAI','CSMA')
#""")
#conn.commit()

# Search /Retrieve
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1 ")
data = mycursor.fetchall()
print(data)

#update
mycursor.execute("""
UPDATE airport
SET name = 'Bombay'
WHERE airport_id = 3
""")
can.commit()

mycursor.execute("SELECT * FROM airport  ")
data = mycursor.fetchall()
print(data)