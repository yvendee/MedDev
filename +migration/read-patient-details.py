import mysql.connector

def read_patient_details():
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

        # SQL query to select all data from the "patient_details" table
        select_query = """
        SELECT * FROM patient_details
        """

        # Executing the SQL query
        cursor.execute(select_query)

        # Fetching all rows
        rows = cursor.fetchall()

        # Replace None values with empty strings
        formatted_rows = []
        for row in rows:
            formatted_row = tuple("" if col is None else col for col in row)
            formatted_rows.append(formatted_row)

        return formatted_rows

    except mysql.connector.Error as error:
        print("Error reading data:", error)
        return None

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage
patient_details = read_patient_details()
if patient_details:
    print("Patient details:")
    for row in patient_details:
        print(row)
else:
    print("Failed to read patient details.")
