import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="testing"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM estudent WHERE name LIKE '%juliao%'")

result = mycursor.fetchone()

for x in result:
    print(x)
