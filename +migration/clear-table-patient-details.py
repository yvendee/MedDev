import mysql.connector

def clear_patient_details():
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
            return False

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to clear all data from the "patient_details" table
        delete_query = """
        DELETE FROM patient_details
        """

        # Executing the SQL query
        cursor.execute(delete_query)

        # Committing the changes
        connection.commit()

        print("All data cleared from the 'patient_details' table!")
        return True

    except mysql.connector.Error as error:
        print("Error clearing data:", error)
        return False

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage
clear_successful = clear_patient_details()
if clear_successful:
    print("Data cleared successfully!")
else:
    print("Failed to clear data.")
