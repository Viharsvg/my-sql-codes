import mysql.connector
con=mysql.connector.connect(host="localhost",
                            user="root",
                            password="root",
                            database="vihar")

if con.is_connected():
    print("connected to sql succesfully")
cur=con.cursor()
cur.execute("select * from student")


data=cur.fetchmany(11)
for i in data:
    print (i)
print("total number of rows retrieved=",cur.rowcount)





