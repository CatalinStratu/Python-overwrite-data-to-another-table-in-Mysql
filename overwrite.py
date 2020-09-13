# Connect to MySQL
import mysql
import mysql.connector
# creating a connection
cnx = mysql.connector.connect(
    user='root', password='password', database='db_name', host='localhost')

cursor = cnx.cursor()
query = ("INSERT INTO tablenew(name, owner_id) SELECT name, id FROM tableold;")
# With WHERE
#query = ("INSERT INTO tablenew(name, owner_id) SELECT name, id FROM tableold WHERE type='1';")
# SQL query execution
cursor.execute(query)
# Data is commited to Database
cnx.commit()
# close connection
cursor.close()
cnx.close()
print("Success!!!")
