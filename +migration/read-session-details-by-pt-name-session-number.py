import mysql.connector

def read_session_data(pt, firstname, lastname, session_number):
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

        # SQL query to read session data based on pt, firstname, lastname, and session_number
        select_query = """
        SELECT l1, l2, l3, l4, l5, r1, r2, r3, r4, r5
        FROM session_details
        WHERE pt = %s AND firstname = %s AND lastname = %s AND session_number = %s
        """

        # Executing the SQL query
        cursor.execute(select_query, (pt, firstname, lastname, session_number))

        # Fetching the row
        session_data = cursor.fetchone()

        if session_data:
            # Extracting the required fields and returning as a list
            return list(session_data)
        else:
            print("No data found for the specified session")
            return None

    except mysql.connector.Error as error:
        print("Error reading session data:", error)
        return None

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage: Read session data and extract required fields
session_data = read_session_data("helloworld", "john", "dee", "Session1")
print(session_data)