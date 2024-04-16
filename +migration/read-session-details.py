import mysql.connector

def read_all_data():
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

        # SQL query to select all records from the "session_details" table
        select_query = "SELECT * FROM session_details"

        # Executing the SQL query
        cursor.execute(select_query)

        # Fetching all records from the result set
        records = cursor.fetchall()

        # Printing all records
        for record in records:
            print(record)

    except mysql.connector.Error as error:
        print("Error reading data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()


# Read all data from the "session_details" table
read_all_data()
