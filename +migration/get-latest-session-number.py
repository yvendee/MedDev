import mysql.connector

def get_latest_session_details(pt, firstname, lastname):
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

        # Query to retrieve the latest session number for the given pt, firstname, and lastname
        latest_session_query = f"""
        SELECT session_number
        FROM session_details
        WHERE pt = '{pt}'
        AND firstname = '{firstname}'
        AND lastname = '{lastname}'
        ORDER BY session_number DESC
        LIMIT 1
        """

        # Executing the SQL query
        cursor.execute(latest_session_query)

        # Fetch the latest session number
        latest_session_number = cursor.fetchone()

        return latest_session_number[0] if latest_session_number else None

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        # Closing the cursor
        if cursor:
            cursor.close()
        # Closing the connection
        if connection.is_connected():
            connection.close()


pt = "helloworld"
firstname = "john"
lastname = "dee"

# pt = "helloworld"
# firstname = "sarah"
# lastname = "dee"

# Get the latest session number for the given pt, firstname, and lastname
latest_session_number = get_latest_session_details(pt, firstname, lastname)

print("Latest Session Number:", latest_session_number)

if(latest_session_number == None):
    print("not found!")