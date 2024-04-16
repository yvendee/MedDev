import mysql.connector

def create_patient_details_table():
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

        # SQL query to create the "patient_details" table with TEXT data type for all columns
        create_table_query = """
        CREATE TABLE patient_details (
            id INT AUTO_INCREMENT PRIMARY KEY,
            pt TEXT,
            firstname TEXT,
            lastname TEXT,
            age TEXT,
            startoftherapy TEXT,
            totalsession TEXT,
            lastsession TEXT,
            status TEXT,
            physician TEXT
        )
        """

        # Executing the SQL query
        cursor.execute(create_table_query)

        print("Table 'patient_details' created successfully!")

    except mysql.connector.Error as error:
        print("Error creating table:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Create the "patient_details" table
create_patient_details_table()
