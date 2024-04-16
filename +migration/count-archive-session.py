import mysql.connector

def count_entries(pt, firstname, lastname):
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
            return "Connection failed"

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to count the entries based on "pt", "firstname", and "lastname"
        count_query = """
        SELECT COUNT(*) 
        FROM archive_session 
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Data for the query
        data = (pt, firstname, lastname)

        # Executing the SQL query
        cursor.execute(count_query, data)

        # Fetching the count result
        count_result = cursor.fetchone()[0]

        return count_result

    except mysql.connector.Error as error:
        return f"Error counting entries: {error}"

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage:
pt = "helloworld"
firstname = "john"
lastname = "dee"

# Count the entries for the specified "pt", "firstname", and "lastname"
result = count_entries(pt, firstname, lastname)
print(result)
