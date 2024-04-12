import mysql.connector

def extract_patient_data_by_id(id_value):
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

        # SQL query to select data from the "patient_active" table by id
        select_query = """
        SELECT pt, firstname, lastname
        FROM patient_active
        WHERE id = %s
        """
        
        # Execute the SQL query
        cursor.execute(select_query, (id_value,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        if result:
            # Convert the result tuple to a list of strings
            result_list = list(map(str, result))
            return result_list
        else:
            print("No data found for id =", id_value)
            return None

    except mysql.connector.Error as error:
        print("Error extracting data:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
data = extract_patient_data_by_id(1)
if data:
    print(data)  # Output: ["pt", "firstname", "lastname"]
