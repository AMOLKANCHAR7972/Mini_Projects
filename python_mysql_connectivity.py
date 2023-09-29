# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 17:17:24 2023

@author: amolk
"""
#####################BookStore######################

#pip install mysql-connector-python

# Connecting to Mysql and Creating Database
import mysql.connector


    
mydb= mysql.connector.connect(
      host='localhost',
      user='root',
      password='7452'
    )
print(mydb.connection_id) 

cur= mydb.cursor()
cur.execute("create database db1")

try:
# Connecting Mysql Database and Creating Table
    mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='7452',
    database='db1'
    )
    cur= mydb.cursor()
    table= "create table book(\
            Id int auto_increment primary key,\
            Bookid int,\
            Title varchar(20),\
            Author varchar(20),\
            Date_of_purchase Date,\
            Price float(8,2))"
    cur.execute(table)

# Create a New Record
    record =int(input("No of records= "))

    for rec in range(record):
    
        insert_query="insert into book (Bookid,Title,Author,Date_of_purchase,Price) values(%s,%s,%s,%s,%s)"
        book=input("Enter Bookid= "),input("Enter Book Title= "),input("Enter the Author Name= "),input("Enter Dateofpurchase(YYYY-MM-DD)= "),input("Enter Price= ")
        print()
        cur.execute(insert_query,book)
        mydb.commit()
    print("Record inserted")

# Fetchall Records
    q= "select * from book"
    cur.execute(q)
    result= cur.fetchall()

    print("List of Records:- ")
    for record in result:
        print(record)
    
# Update a Book Record
    update_query= "update book set price=%s where bookid=%s"
    up= input("price= "),input("bookid= ")
    cur.execute(update_query,up)
    mydb.commit()
    print("Record Updated")

# Delete a Book Record
    delete_query= "delete from book where bookid=%s"
    bid= input("bookid= ")
    cur.execute(delete_query,(bid,))
    mydb.commit()
    print("Record Deleted")

except mysql.connector.Error as err:
    print(err)

finally:
    # Close the cursor and connection
    if mydb.is_connected():
        cur.close()
        mydb.close()
