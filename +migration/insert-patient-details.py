import mysql.connector

def insert_patient_details(pt, firstname, lastname, age, startoftherapy):
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
            return False

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # Check if the record already exists based on first name and last name
        check_query = """
        SELECT COUNT(*) FROM patient_details WHERE firstname = %s AND lastname = %s
        """
        cursor.execute(check_query, (firstname, lastname))
        count = cursor.fetchone()[0]

        # If count is greater than 0, a record with the same first name and last name already exists
        if count > 0:
            print("Duplicate entry for patient:", firstname, lastname)
            return False

        # SQL query to insert new data into the "patient_details" table
        insert_query = """
        INSERT INTO patient_details (pt, firstname, lastname, age, startoftherapy)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Data to be inserted
        data = (pt, firstname, lastname, age, startoftherapy)

        # Executing the SQL query with data as parameters
        cursor.execute(insert_query, data)

        # Committing the changes
        connection.commit()

        print("Data inserted successfully!")
        return True

    except mysql.connector.Error as error:
        print("Error inserting data:", error)
        return False

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# # Example usage
# pt = "helloworld"  # Example physical therapist
# firstname = "John"
# lastname = "Doe"
# age = 30
# startoftherapy = "2024-04-15"  # Format: YYYY-MM-DD
# insert_successful = insert_patient_details(pt, firstname, lastname, age, startoftherapy)
# if insert_successful:
#     print("Data inserted successfully!")
# else:
#     print("Failed to insert data.")
