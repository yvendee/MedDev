import mysql.connector

def read_data():
    data_list = []
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

        # SQL query to select all data from the "grip_signup" table
        select_query = "SELECT * FROM grip_signup"

        # Execute the SQL query
        cursor.execute(select_query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Append each row to the data list
        for row in rows:
            # Convert each row to a list and append to data_list
            data_list.append([str(row[0])] + list(row)[1:])

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    return data_list

# Example usage
data = read_data()
print(data)
