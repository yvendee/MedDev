import mysql.connector

def create_table():
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

            # SQL query to create a new table "grip_active" with the new column "ptlastname"
            create_table_query = """
            CREATE TABLE grip_active (
                role VARCHAR(255),
                ptname VARCHAR(255),
                ptlastname VARCHAR(255),
                status VARCHAR(255)
            )
            """

            # Execute the SQL query
            cursor.execute(create_table_query)

            print("Table 'grip_active' created successfully!")

    except mysql.connector.Error as error:
        print("Error creating table:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
create_table()
