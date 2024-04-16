import mysql.connector

def delete_archive_session_table():
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

        # SQL query to delete the "archive_session" table
        delete_table_query = """
        DROP TABLE IF EXISTS archive_session
        """

        # Executing the SQL query
        cursor.execute(delete_table_query)

        print("Table 'archive_session' deleted successfully!")

    except mysql.connector.Error as error:
        print("Error deleting table:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Delete the "archive_session" table
delete_archive_session_table()
