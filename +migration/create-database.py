import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Create cursor
mycursor = mydb.cursor()

# Execute SQL command to create the database
mycursor.execute("CREATE DATABASE gripdespro")

# Close cursor and connection
mycursor.close()
mydb.close()
