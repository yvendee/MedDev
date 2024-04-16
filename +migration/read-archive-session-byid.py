import mysql.connector

def extract_data(pt, firstname, lastname):
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

        # SQL query to fetch data for the specified columns and filter by pt, firstname, and lastname
        select_query = """
        SELECT date, hand, f1, f2, f3, f4, f5
        FROM archive_session
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Executing the SQL query with parameters
        cursor.execute(select_query, (pt, firstname, lastname))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Creating a list to store extracted data
        data = []

        # Iterating over the rows and appending the required columns to the data list
        for row in rows:
            data.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])

        return data

    except mysql.connector.Error as error:
        print("Error extracting data:", error)

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
data = extract_data(pt, firstname, lastname)

# Print the extracted data
for row in data:
    print(row)
