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

    # SQL query to create a table named "grip_signup" with TEXT data type for columns
    create_table_query = """
    CREATE TABLE grip_signup (
        id INT AUTO_INCREMENT PRIMARY KEY,
        firstname TEXT,
        lastname TEXT,
        password TEXT
    )
    """

    # Execute the SQL query
    cursor.execute(create_table_query)

    # Committing the changes
    connection.commit()

    print("Table 'grip_signup' created successfully!")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    # Closing the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
