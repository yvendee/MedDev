import mysql.connector

def update_session_active_data(id, new_session):
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

        # SQL query to update the "current_session" column in the "session_active" table
        update_query = """
        UPDATE session_active
        SET current_session = %s
        WHERE id = %s
        """

        # Data for update
        data = (new_session, id)

        # Executing the SQL query with data
        cursor.execute(update_query, data)

        # Committing the changes
        connection.commit()

        print("Data updated successfully!")

    except mysql.connector.Error as error:
        print("Error updating data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage:
update_session_active_data(1, "Session1")
