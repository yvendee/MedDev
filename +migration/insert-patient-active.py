import mysql.connector

def insert_patient_data(pt, firstname, lastname):
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

            # SQL query to insert data into the "patient_active" table
            insert_query = """
            INSERT INTO patient_active (pt, firstname, lastname)
            VALUES (%s, %s, %s)
            """
            # Data to be inserted
            data = (pt, firstname, lastname)

            # Execute the SQL query
            cursor.execute(insert_query, data)

            # Commit the changes
            connection.commit()

            print("Data inserted successfully")

    except mysql.connector.Error as error:
        print("Error inserting data:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
# insert_patient_data("helloworldx", "john", "dee")
insert_patient_data("helloworld", "john", "dee")
