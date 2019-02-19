import mysql.connector


mydb = mysql.connector.connect(host='localhost', user='root', passwd='password', database='motech_data_services')

mycursor = mydb.cursor()

mycursor.execute("select * from wash_states limit 1;")

for i in mycursor:
	print(i)