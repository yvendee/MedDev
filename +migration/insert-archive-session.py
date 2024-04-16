import mysql.connector

def insert_archive_session_data(pt, firstname, lastname, date, hand, f1, f2, f3, f4, f5):
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

        # SQL query to insert data into the "archive_session" table
        insert_query = """
        INSERT INTO archive_session (pt, firstname, lastname, date, hand, f1, f2, f3, f4, f5) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Data to be inserted
        data = (pt, firstname, lastname, date, hand, f1, f2, f3, f4, f5)

        # Executing the SQL query
        cursor.execute(insert_query, data)

        # Committing the changes to the database
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
pt = "helloworld"
firstname = "john"
lastname = "dee"
date = "2024-04-16"
# hand = "Right"
hand = "left"
f1 = "10"
f2 = "20"
f3 = "30"
f4 = "40"
f5 = "50"

# Insert data into the "archive_session" table
# insert_archive_session_data(pt, firstname, lastname, date, hand, f1, f2, f3, f4, f5)
insert_archive_session_data(pt, firstname, lastname, date, hand, f1, f2, f3, f4, f5)
