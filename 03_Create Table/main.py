import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="root",
        database="testing"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE estudent (name VARCHAR(255), email VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#    print(x)

mycursor.execute("ALTER TABLE estudent ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
