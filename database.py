import pymysql
connection = pymysql.connect(host="localhost",user="root",password="",db="doccollection")
mycursor = connection.cursor()
#mycursor.execute(""" create table docdetail
#(
   
#doctor varchar(1000)


#)
#""")

mycursor.execute("insert into docdetail(doctor) value ('Dr.Saurabh Maurya (Mbbs)')")

connection.commit()
connection.close()