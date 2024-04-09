import mysql.connector

def read_all_data():
    result = []  # List to store the fetched data
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

            # SQL query to select all data from the "grip_active" table
            select_query = "SELECT * FROM grip_active"

            # Execute the SQL query
            cursor.execute(select_query)

            # Fetch the first row
            row = cursor.fetchone()

            # If a row is fetched, append it to the result list
            if row:
                result.append(list(row))

    except mysql.connector.Error as error:
        print("Error reading data:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    return result

# Example usage
data = read_all_data()
print(data)
