import mysql.connector

def delete_session_details_table():
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

        # SQL query to delete the "session_details" table
        delete_table_query = "DROP TABLE IF EXISTS session_details"

        # Executing the SQL query
        cursor.execute(delete_table_query)

        print("Table 'session_details' deleted successfully!")

    except mysql.connector.Error as error:
        print("Error deleting table:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

delete_session_details_table()
