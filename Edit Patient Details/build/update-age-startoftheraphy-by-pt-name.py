import mysql.connector

def update_age_startoftherapy(pt, firstname, lastname, new_age, new_startoftherapy):
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
            return False  # Return False if connection fails

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to update age and startoftherapy based on pt, firstname, and lastname
        update_query = """
        UPDATE patient_details
        SET age = %s, startoftherapy = %s
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Executing the SQL query with the provided parameters
        cursor.execute(update_query, (new_age, new_startoftherapy, pt, firstname, lastname))

        # Committing the changes
        connection.commit()

        # Check if any row was affected
        if cursor.rowcount > 0:
            print("Age and Start of Therapy updated successfully.")
            return True
        else:
            print("No matching record found.")
            return False

    except mysql.connector.Error as error:
        print("Error:", error)
        return False  # Return False if an error occurs

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage:
updated = update_age_startoftherapy("helloworld", "sarah", "see", "30", "2024-04-12")
print("Update successful:", updated)