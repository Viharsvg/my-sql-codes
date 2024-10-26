import mysql.connector
con=mysql.connector.connect(host="localhost",
                             user="root",
                             password="root")
con.is_connected()
print("connected to sql succesfully")
cur=con.cursor()
cur.execute("create database student")
print("database created succesfullyyyyyy")

