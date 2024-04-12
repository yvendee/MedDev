import mysql.connector

def extract_status():
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
            return None

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to select status value from the grip_active table
        select_query = """
        SELECT status FROM grip_active LIMIT 1
        """

        # Executing the SQL query
        cursor.execute(select_query)

        # Fetching the status value
        status_value = cursor.fetchone()

        if status_value:
            return int(status_value[0])
        else:
            print("No status value found in the grip_active table")
            return None

    except mysql.connector.Error as error:
        print("Error:", error)
        return None

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage
status = extract_status()
print("Status:", status)
