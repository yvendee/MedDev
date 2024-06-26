import mysql.connector

def update_record(role, ptname, ptlastname, status):
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

            # Update query
            update_query = """
            UPDATE grip_active 
            SET role=%s, ptname=%s, ptlastname=%s, status=%s
            LIMIT 1
            """

            # Execute the SQL query
            cursor.execute(update_query, (role, ptname, ptlastname, status))
            connection.commit()

            print("Record updated successfully")

    except mysql.connector.Error as error:
        print("Error updating record:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
update_record("Updated Role", "Updated Ptname", "Updated Ptlastname", "Updated Status")
