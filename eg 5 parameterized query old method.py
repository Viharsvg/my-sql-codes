import mysql.connector
con=mysql.connector.connect(host="localhost",
                            user="root",
                            password="root",
                            database="vihar")

if con.is_connected():
    print("connected to sql succesfully")
cur=con.cursor()


p=float(input("enter the percentage"))
s=input("enter the streams")
query="select * from student where per>%s and stream='%s'"%(p,s)
cur.execute(query)
    
data=cur.fetchall()
for i in data:
    print (i)
