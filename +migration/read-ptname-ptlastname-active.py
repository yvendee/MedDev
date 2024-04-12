import mysql.connector

def extract_ptname_ptlastname():
    pt_info = []  # List to store ptname and ptlastname
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

            # Select query to fetch ptname and ptlastname
            select_query = "SELECT ptname, ptlastname FROM grip_active LIMIT 1"

            # Execute the SQL query
            cursor.execute(select_query)

            # Fetch the first row
            row = cursor.fetchone()

            if row:
                pt_info = list(row)

    except mysql.connector.Error as error:
        print("Error fetching data:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    return pt_info

# Example usage
ptname_ptlastname = extract_ptname_ptlastname()
print(ptname_ptlastname)
