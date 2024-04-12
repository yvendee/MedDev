import mysql.connector

def read_patient_data():
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

            # SQL query to select all data from the "patient_active" table
            select_query = "SELECT * FROM patient_active"

            # Execute the SQL query
            cursor.execute(select_query)

            # Fetch all rows
            rows = cursor.fetchall()

            # Print the data
            for row in rows:
                print(row)

    except mysql.connector.Error as error:
        print("Error reading data:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Call the function to read data
read_patient_data()
