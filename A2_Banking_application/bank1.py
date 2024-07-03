import pymysql

#connection with server

mydb=pymysql.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()

#need to create database

mycursor.execute("create database if not exists python_crud1")
mydb.commit()
# print("Database created")

# connection with database

mydb=pymysql.connect(host="localhost",user="root",password="",database="python_crud1")
mycursor=mydb.cursor()

# table creation

mycursor.execute("create table if not exists bank(name varchar(50),account_type varchar(50),account_number int PRIMARY KEY,password varchar(50))")

mydb.commit()
# print("Table creation successfully") 
# # importing connection file

