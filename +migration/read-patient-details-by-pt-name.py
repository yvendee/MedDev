import mysql.connector

def extract_columns_from_patient_details(pt, firstname, lastname):
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
            return ["", "", "", ""]  # Return empty list if connection fails

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to select specific columns from the "patient_details" table based on pt, firstname, and lastname
        select_query = """
        SELECT age, startoftherapy, totalsession, physician
        FROM patient_details
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Executing the SQL query with the provided parameters
        cursor.execute(select_query, (pt, firstname, lastname))

        # Fetching the first row from the result
        row = cursor.fetchone()

        if row:
            # Convert None values to empty strings
            age, startoftherapy, totalsession, physician = map(lambda x: x if x is not None else "", row)
            return [age, startoftherapy, totalsession, physician]  # Return list with extracted data
        else:
            return ["", "", "", ""]  # Return empty list if no matching patient found

    except mysql.connector.Error as error:
        print("Error:", error)
        return ["", "", "", ""]  # Return empty list if error occurs

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage:
result = extract_columns_from_patient_details("helloworld", "sarah", "dee")
print(result)
