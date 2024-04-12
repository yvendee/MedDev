import mysql.connector

def update_patient_data(new_pt, new_firstname, new_lastname, id_value):
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

        # SQL query to update the data in the "patient_active" table
        update_query = """
        UPDATE patient_active
        SET pt = %s, firstname = %s, lastname = %s
        WHERE id = %s
        """
        # Data to be updated
        data = (new_pt, new_firstname, new_lastname, id_value)

        # Execute the SQL query
        cursor.execute(update_query, data)

        # Commit the changes
        connection.commit()

        print("Data updated successfully")

    except mysql.connector.Error as error:
        print("Error updating data:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
update_patient_data("helloworldx", "john2", "dee2", 1)
