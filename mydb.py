import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Ranjan@1990'
	)


#Prepare a Cursor Object
cursorObject = dataBase.cursor()

#Create a Database
cursorObject.execute("CREATE DATABASE sourabhmysql")

print("All Done")

