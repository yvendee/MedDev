import mysql.connector


import mysql.connector

def get_current_session_by_id(id):
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

        # SQL query to select the "current_session" value by id
        select_query = """
        SELECT current_session
        FROM session_active
        WHERE id = %s
        """

        # Executing the SQL query with parameter
        cursor.execute(select_query, (id,))

        # Fetching the result
        result = cursor.fetchone()

        if result:
            current_session = result[0]
            return current_session
            # print("Current session value:", current_session)
        else:
            print("No data found for id:", id)

    except mysql.connector.Error as error:
        print("Error fetching data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def get_latest_session_details(pt, firstname, lastname):
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

        # Query to retrieve the latest session number for the given pt, firstname, and lastname
        latest_session_query = f"""
        SELECT session_number
        FROM session_details
        WHERE pt = '{pt}'
        AND firstname = '{firstname}'
        AND lastname = '{lastname}'
        ORDER BY session_number DESC
        LIMIT 1
        """

        # Executing the SQL query
        cursor.execute(latest_session_query)

        # Fetch the latest session number
        latest_session_number = cursor.fetchone()

        return latest_session_number[0] if latest_session_number else None

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        # Closing the cursor
        if cursor:
            cursor.close()
        # Closing the connection
        if connection.is_connected():
            connection.close()


def extract_columns_from_patient_details(pt, firstname, lastname):
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
            return ["", "", "", ""]  # Return empty list if connection fails

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to select specific columns from the "patient_details" table based on pt, firstname, and lastname
        select_query = """
        SELECT age, startoftherapy, totalsession, physician
        FROM patient_details
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Executing the SQL query with the provided parameters
        cursor.execute(select_query, (pt, firstname, lastname))

        # Fetching the first row from the result
        row = cursor.fetchone()

        if row:
            # Convert None values to empty strings
            age, startoftherapy, totalsession, physician = map(lambda x: x if x is not None else "", row)
            return [age, startoftherapy, totalsession, physician]  # Return list with extracted data
        else:
            return ["", "", "", ""]  # Return empty list if no matching patient found

    except mysql.connector.Error as error:
        print("Error:", error)
        return ["", "", "", ""]  # Return empty list if error occurs

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()


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


def read_session_data(pt, firstname, lastname, session_number):
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
            return None

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to read session data based on pt, firstname, lastname, and session_number
        select_query = """
        SELECT l1, l2, l3, l4, l5, r1, r2, r3, r4, r5
        FROM session_details
        WHERE pt = %s AND firstname = %s AND lastname = %s AND session_number = %s
        """

        # Executing the SQL query
        cursor.execute(select_query, (pt, firstname, lastname, session_number))

        # Fetching the row
        session_data = cursor.fetchone()

        if session_data:
            # Extracting the required fields and returning as a list
            return list(session_data)
        else:
            # print("No data found for the specified session")
            return None

    except mysql.connector.Error as error:
        print("Error reading session data:", error)
        return None

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()




edata = extract_patient_data_by_id(1)
# print(edata)
# if data:
#     print(data)  # Output: ["pt", "firstname", "lastname"]

import mysql.connector

def get_current_session_by_id(id):
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

        # SQL query to select the "current_session" value by id
        select_query = """
        SELECT current_session
        FROM session_active
        WHERE id = %s
        """

        # Executing the SQL query with parameter
        cursor.execute(select_query, (id,))

        # Fetching the result
        result = cursor.fetchone()

        if result:
            current_session = result[0]
            # print("Current session value:", current_session)
            return current_session
        else:
            print("No data found for id:", id)

    except mysql.connector.Error as error:
        print("Error fetching data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage:
rtn = get_current_session_by_id(1)

# print(rtn)

# latest_session_number = get_latest_session_details(edata[0], edata[1], edata[2])
# print(latest_session_number)

# print(edata)

# # Example usage:
result = extract_columns_from_patient_details(edata[0], edata[1], edata[2])
# # print(result) # age, startoftherapy, totalsession, physician

session_str = get_current_session_by_id(1)

# session_str = latest_session_number

# Example usage: Read session data and extract required fields
session_data = read_session_data(edata[0], edata[1], edata[2], session_str)

# session_data = read_session_data("helloworld", "john", "dee", "Session1")
if(session_data == None):
    # print("empty")
    session_data = ["","","","","","","","","",""]
# print(session_data)

# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("900x600")
window.geometry("+10+10")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

canvas.create_text(
    360.0,
    152.0,
    anchor="nw",
    text=session_str,
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_1 clicked"), window.destroy()],
    relief="flat"
)
button_1.place(
    x=703.6898803710938,
    y=535.0,
    width=146.14328002929688,
    height=36.0
)

canvas.create_text(
    63.0,
    222.0,
    anchor="nw",
    text=result[0],
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_text(
    63.0,
    276.0,
    anchor="nw",
    text=result[1],
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_text(
    63.0,
    337.0,
    anchor="nw",
    text=result[2],
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_text(
    63.0,
    407.0,
    anchor="nw",
    text=edata[0],
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_text(
    60.0,
    98.0,
    anchor="nw",
    text=edata[2],
    fill="#FFFFFF",
    font=("Inter Bold", 40 * -1)
)

canvas.create_text(
    60.0,
    59.0,
    anchor="nw",
    text=edata[1],
    fill="#FFFFFF",
    font=("Inter Bold", 40 * -1)
)

canvas.create_text(
    626.0,
    267.0,
    anchor="nw",
    text=session_data[5],
    fill="#FFFFFF",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    377.0,
    315.0,
    anchor="nw",
    text=str(session_data[0]),
    fill="#FFFFFF",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    422.0,
    224.0,
    anchor="nw",
    text=str(session_data[1]),
    fill="#FFFFFF",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    480.0,
    211.0,
    anchor="nw",
    text=str(session_data[2]),
    fill="#FFFFFF",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    534.0,
    229.0,
    anchor="nw",
    text=str(session_data[3]),
    fill="#FFFFFF",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    573.0,
    267.0,
    anchor="nw",
    text=str(session_data[4]),
    fill="#FFFFFF",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    664.0,
    229.0,
    anchor="nw",
    text=str(session_data[6]),
    fill="#FFFFFF",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    714.0,
    211.0,
    anchor="nw",
    text=str(session_data[7]),
    fill="#FFFFFF",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    769.0,
    224.0,
    anchor="nw",
    text=str(session_data[8]),
    fill="#FFFFFF",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    815.0,
    315.0,
    anchor="nw",
    text=str(session_data[9]),
    fill="#FFFFFF",
    font=("Inter SemiBold", 15 * -1)
)
window.resizable(False, False)
window.mainloop()
