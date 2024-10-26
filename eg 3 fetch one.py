import mysql.connector
con=mysql.connector.connect(host="localhost",
                            user="root",
                            password="root",
                            database="vihar")

if con.is_connected():
    print("connected to sql succesfully")
cur=con.cursor()
cur.execute("select * from student")

#this statement will fetch one record 1
data=cur.fetchone()
print (data)
print("total number of rows retrieved=",cur.rowcount)

#this statement will fetch one record 2
data=cur.fetchone()
print (data)
print("total number of rows retrieved=",cur.rowcount)




