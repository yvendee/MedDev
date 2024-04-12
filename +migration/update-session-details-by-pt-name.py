import mysql.connector

def extract_session_data(pt, firstname, lastname):
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
            return []

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to extract session data based on pt, firstname, and lastname
        select_query = """
        SELECT session_number, l1, l2, l3, l4, l5, r1, r2, r3, r4, r5
        FROM session_details
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Executing the SQL query
        cursor.execute(select_query, (pt, firstname, lastname))

        # Fetching all the rows
        session_data = cursor.fetchall()

        extracted_data = []
        # Appending each session's data to the list
        for session in session_data:
            extracted_data.append(list(session))

        return extracted_data

    except mysql.connector.Error as error:
        print("Error extracting session data:", error)
        return []

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage: Extract session data for a specific patient
session_data = extract_session_data("helloworld", "john", "dee")
print(session_data)