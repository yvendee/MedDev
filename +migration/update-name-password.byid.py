import mysql.connector

def update_user_info(user_id, new_firstname, new_lastname, new_password):
    try:
        # Establishing the connection to MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gripdespro"
        )

        if not connection.is_connected():
            print("Connection failed")
            return False

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to update firstname, lastname, and password based on id
        update_query = """
        UPDATE grip_signup
        SET firstname = %s, lastname = %s, password = %s
        WHERE id = %s
        """

        # Executing the SQL query with new values and user_id as parameters
        cursor.execute(update_query, (new_firstname, new_lastname, new_password, user_id))

        # Committing the changes
        connection.commit()

        print("User information updated successfully!")
        return True

    except mysql.connector.Error as error:
        print("Error:", error)
        return False

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage
user_id = 1  # Change this to the desired user ID
new_firstname = "NewJohn"  # Change this to the new firstname
new_lastname = "NewDoe"    # Change this to the new lastname
new_password = "newpassword"  # Change this to the new password
update_successful = update_user_info(user_id, new_firstname, new_lastname, new_password)
if update_successful:
    print("User information updated successfully!")
else:
    print("Failed to update user information.")
