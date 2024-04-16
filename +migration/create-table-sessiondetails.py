import mysql.connector

def create_session_details_table():
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

        # SQL query to create the "session_details" table with TEXT data type for all columns
        create_table_query = """
        CREATE TABLE session_details (
            id INT AUTO_INCREMENT PRIMARY KEY,
            pt TEXT,
            firstname TEXT,
            lastname TEXT,
            session_number TEXT,
            l1 TEXT,
            l2 TEXT,
            l3 TEXT,
            l4 TEXT,
            l5 TEXT,
            r1 TEXT,
            r2 TEXT,
            r3 TEXT,
            r4 TEXT,
            r5 TEXT
        )
        """

        # Executing the SQL query
        cursor.execute(create_table_query)

        print("Table 'session_details' created successfully!")

    except mysql.connector.Error as error:
        print("Error creating table:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Create the "session_details" table
create_session_details_table()
