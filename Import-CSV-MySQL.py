#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Importing CSV
import pandas as pd
empdata = pd.read_csv(r"C:\Users\ASUS\Downloads\us-500\us-500.csv", index_col=False, delimiter = ',')
empdata.head()


# In[2]:


##Database Conenction
import mysql.connector as mysql
from mysql.connector import Error
try:
    conn = mysql.connect(host='localhost', database='employee', user='root', password='root2x5=10')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
     
        #loop through the data frame
        for i,row in empdata.iterrows():
            #Insert Query 
            sql = "INSERT INTO employee.employee_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)

