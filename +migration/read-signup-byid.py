import mysql.connector

def get_name_by_id(user_id):
    try:
        # Establishing the connection to MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gripdespro"
        )

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to select firstname and lastname based on id
        select_query = """
        SELECT firstname, lastname FROM grip_signup WHERE id = %s
        """

        # Executing the SQL query with user_id as parameter
        cursor.execute(select_query, (user_id,))

        # Fetching the result
        result = cursor.fetchone()

        if result:
            firstname, lastname = result
            return [firstname, lastname]
        else:
            return None

    except mysql.connector.Error as error:
        print(f"Error: {error}")
        return None

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
user_id = 1  # Change this to the desired user ID
name_list = get_name_by_id(user_id)
print(name_list)  # Output the list containing firstname and lastname
