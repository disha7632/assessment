import connection

import pymysql

mydb1=pymysql.connect(host="localhost",user="root",password="",database="python_crud1")
mycursor=mydb1.cursor()

status=True

while status:

    menu="""
            Menu

            1) Store data
            2) View data
            3) Update data
            4) Search data
            5) Delete data

        """
    
    print(menu)

    choice=int(input("Enter Your Choice:"))
    if choice==1:
        #to insert data
        name=input("Enter your name:")
        account_type=input("Enter your account type:")
        account_number=int(input("Enter your account number:"))
        password=int(input("Enter Your password:"))

        query="insert into bank(name,account_type,account_number,password) values('%s','%s',%s,%s)"
        args=(name,account_type,account_number,password)

        mycursor.execute(query % args)

        #to save changes
        mydb1.commit()
        print("Data Inserted Successfully")

    elif choice==2:
        #to fatch all data from table
        query="select * from bank"

        mycursor.execute(query)

        # to fetch all data from query

        data=mycursor.fetchall()
        print(data)

    elif choice==3:
        #update data

        account_number=int(input("Enter Your account number:"))
        name=input("Enter your name:")
        account_type=input("Enter your account type:")
        password=int(input("Enter your password:"))

        query="Update bank set name='%s', account_type='%s',password=%s where account_number=%s"
        args=(name,account_type,password,account_number)

        mycursor.execute(query % args)

        mydb1.commit()
        print("Data Updated Successfully")

    elif choice==4:
        # search data

        account_number=int(input("Enter Your account number:"))

        query="select * from bank where account_number=%s"

        args=(account_number)

        mycursor.execute(query % args)

        #retrieve all data in row variable
        row=mycursor.fetchone()

        #name=0 account_type=1 account_number=2  password=4

        displayname=row[0]
        displayaccount_type=row[1]
        displayaccount_number=row[2]
        displaypassword=row[3]

        print("Name= ",displayname)
        print("account number= ",displayaccount_number)
        print("account type= ",displayaccount_type)
        print("password= ",displaypassword)

    elif choice==5:
        #delete data

        account_number=int(input("Enter account number:"))


        query="delete from bank where account_number=%s"

        args=(account_number)

        mycursor.execute(query % args)

        mydb1.commit()
        print("Data Deleted Successfully")

    loop_choice=input("Do You want to perform more operation? press 'y' for yes and 'n' for no:")

    if loop_choice=='n' or loop_choice=='no':
        status=False    
        print("Thank You For Visiting Our Bank!")