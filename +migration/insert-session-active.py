import mysql.connector

def insert_session_active_data(pt, firstname, lastname, current_session):
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

        # SQL query to insert data into the "session_active" table
        insert_query = """
        INSERT INTO session_active (pt, firstname, lastname, current_session)
        VALUES (%s, %s, %s, %s)
        """

        # Data to be inserted
        data = (pt, firstname, lastname, current_session)

        # Executing the SQL query with data
        cursor.execute(insert_query, data)

        # Committing the changes
        connection.commit()

        print("Data inserted successfully!")

    except mysql.connector.Error as error:
        print("Error inserting data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage:
insert_session_active_data("helloworld", "john", "dee", "Session1")
