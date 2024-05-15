import mysql.connector

def create_archive_session_table():
    try:
        # Database connection parameters
        host = "localhost"
        user = "root"
        password = ""
        database = "gripdespro"

        # Establishing the connection to MySQL
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if not connection.is_connected():
            print("Connection failed")
            return

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to create the "archive_session" table with TEXT data type for all columns
        create_table_query = """
        CREATE TABLE archive_session (
            id INT AUTO_INCREMENT PRIMARY KEY,
            pt TEXT,
            firstname TEXT,
            lastname TEXT,
            date TEXT,
            hand TEXT,
            f1 TEXT,
            f2 TEXT,
            f3 TEXT,
            f4 TEXT,
            f5 TEXT,
            remarks TEXT
        )
        """

        # Executing the SQL query
        cursor.execute(create_table_query)

        print("Table 'archive_session' created successfully!")

    except mysql.connector.Error as error:
        print("Error creating table:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Create the "archive_session" table
create_archive_session_table()
