import mysql.connector

def update_role(role, new_ptname, new_status):
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

            # SQL query to update data in the "grip_active" table
            update_query = """
            UPDATE grip_active
            SET ptname = %s, status = %s
            WHERE role = %s
            """

            # Data for the update query
            data = (new_ptname, new_status, role)

            # Execute the SQL query
            cursor.execute(update_query, data)

            # Committing the changes
            connection.commit()

            print("Data updated successfully!")

    except mysql.connector.Error as error:
        print("Error updating data:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
update_role("admin", "Tess", "active")
