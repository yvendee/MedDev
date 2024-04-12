import mysql.connector

def extract_data(pt_value):
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

        # SQL query to fetch required columns from the table based on the 'pt' value
        select_query = """
        SELECT firstname, lastname, lastsession, status 
        FROM patient_details 
        WHERE pt = %s
        """

        # Executing the SQL query with the specified 'pt' value
        cursor.execute(select_query, (pt_value,))

        # Fetching all rows from the result set
        rows = cursor.fetchall()

        # Formatting the data into the desired output format
        output_data = [[row[0], row[1], row[2] if row[2] else "", row[3] if row[3] else ""] for row in rows]

        return output_data

    except mysql.connector.Error as error:
        print("Error extracting data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Specify the 'pt' value for extraction
pt_value = "helloxworldx"

# Extract the required data
extracted_data = extract_data(pt_value)

# Print the extracted data
mylist = []
for row in extracted_data:
    mylist.append(row)

print(mylist)
