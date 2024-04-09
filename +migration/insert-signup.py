import mysql.connector

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
