import mysql.connector

def insert_mockup_data(pt, firstname, lastname, session_number, l1, l2, l3, l4, l5, r1, r2, r3, r4, r5):
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

        # SQL query to insert mockup data into the session_details table
        insert_query = """
        INSERT INTO session_details (pt, firstname, lastname, session_number, l1, l2, l3, l4, l5, r1, r2, r3, r4, r5)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Executing the SQL query
        cursor.execute(insert_query, (pt, firstname, lastname, session_number, l1, l2, l3, l4, l5, r1, r2, r3, r4, r5))

        # Committing the changes to the database
        connection.commit()

        print("Mockup data inserted successfully!")

    except mysql.connector.Error as error:
        print("Error inserting mockup data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage: Insert mockup data into the session_details table
insert_mockup_data("helloworld", "john", "dee", "Session1", "5", "10", "15", "20", "25", "30", "35", "40", "50", "60")
