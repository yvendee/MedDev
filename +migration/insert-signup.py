import mysql.connector

def check_duplicate(firstname, lastname, cursor):
    # SQL query to check if the firstname and lastname combination exists in the table
    query = """
    SELECT COUNT(*) FROM grip_signup WHERE firstname = %s AND lastname = %s
    """
    # Execute the SQL query with the provided data
    cursor.execute(query, (firstname, lastname))
    # Fetch the result
    result = cursor.fetchone()
    # Return True if the combination already exists, False otherwise
    return result[0] > 0

def insert_data(firstname, lastname, password):
    try:
        # Establishing the connection to MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gripdespro"
        )

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # Check if the firstname and lastname combination already exists
        if check_duplicate(firstname, lastname, cursor):
            print("Error: Duplicate entry detected. This entry already exists in the database.")
        else:
            # SQL query to insert data into the "grip_signup" table
            insert_query = """
            INSERT INTO grip_signup (firstname, lastname, password) 
            VALUES (%s, %s, %s)
            """

            # Data to be inserted
            data = (firstname, lastname, password)

            # Execute the SQL query
            cursor.execute(insert_query, data)

            # Committing the changes
            connection.commit()

            print("Data inserted successfully!")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
insert_data("John", "Doe", "password123")
