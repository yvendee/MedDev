import mysql.connector

# Establishing the connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gripdespro"
)

try:
    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    # SQL query to drop the table named "signin"
    drop_table_query = "DROP TABLE IF EXISTS grip_signup"

    # Execute the SQL query
    cursor.execute(drop_table_query)

    # Committing the changes
    connection.commit()

    print("Table 'grip_signup' deleted successfully!")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    # Closing the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
