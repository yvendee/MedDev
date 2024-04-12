import mysql.connector

def create_patient_active_table():
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

            # SQL query to create the "patient_active" table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS patient_active (
                id INT AUTO_INCREMENT PRIMARY KEY,
                pt VARCHAR(255),
                firstname VARCHAR(255),
                lastname VARCHAR(255)
            )
            """

            # Execute the SQL query
            cursor.execute(create_table_query)

            print("Table 'patient_active' created successfully")

    except mysql.connector.Error as error:
        print("Error creating table:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Call the function to create the table
create_patient_active_table()
