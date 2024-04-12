import mysql.connector

def delete_patient_active_table():
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

        else:
            # Creating a cursor object using the cursor() method
            cursor = connection.cursor()

            # SQL query to delete the "patient_active" table
            delete_query = "DROP TABLE IF EXISTS patient_active"

            # Execute the SQL query
            cursor.execute(delete_query)

            print("Table 'patient_active' deleted successfully")

    except mysql.connector.Error as error:
        print("Error deleting table:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Call the function to delete the table
delete_patient_active_table()
