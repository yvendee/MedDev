import mysql.connector

def create_session_active_table():
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

        # SQL query to create the "session_active" table with specified columns
        create_table_query = """
        CREATE TABLE session_active (
            pt TEXT,
            firstname TEXT,
            lastname TEXT,
            current_session TEXT
        )
        """

        # Executing the SQL query
        cursor.execute(create_table_query)

        print("Table 'session_active' created successfully!")

    except mysql.connector.Error as error:
        print("Error creating table:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Create the "session_active" table
create_session_active_table()
