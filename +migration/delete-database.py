import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

# Create cursor
mycursor = mydb.cursor()

# Execute SQL command to drop the database
mycursor.execute("DROP DATABASE gripdespro")

# Close cursor and connection
mycursor.close()
mydb.close()
