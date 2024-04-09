import mysql.connector

def insert_role():
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
            # Sample data to insert
            role = "admin"
            ptname = "test"
            status = "active"

            # Creating a cursor object using the cursor() method
            cursor = connection.cursor()

            # SQL query to insert data into the "grip_active" table
            insert_query = """
            INSERT INTO grip_active (role, ptname, status)
            VALUES (%s, %s, %s)
            """

            # Data to be inserted
            data = (role, ptname, status)

            # Execute the SQL query
            cursor.execute(insert_query, data)

            # Committing the changes
            connection.commit()

            print("Role inserted successfully!")

    except mysql.connector.Error as error:
        print("Error inserting role:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
insert_role()
