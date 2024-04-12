import mysql.connector

def get_id_by_name(firstname, lastname):
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
            return ""

        else:
            # Creating a cursor object using the cursor() method
            cursor = connection.cursor()

            # SQL query to select id based on firstname and lastname
            select_query = """
            SELECT id FROM grip_signup WHERE firstname = %s AND lastname = %s
            """

            # Executing the SQL query with firstname and lastname as parameters
            cursor.execute(select_query, (firstname, lastname))

            # Fetching the result
            result = cursor.fetchone()

            if result:
                user_id = result[0]
                return user_id
            else:
                print("User not found with firstname:", firstname, "and lastname:", lastname)
                return ""

    except mysql.connector.Error as error:
        print("Error:", error)
        return ""
    except mysql.connector.errors.InternalError as internal_error:
        print("Internal Error:", internal_error)
        return ""
    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage
firstname = "hello"  # Change this to the desired firstname
lastname = "world"    # Change this to the desired lastname
user_id = get_id_by_name(firstname, lastname)
print("User ID:", user_id)
