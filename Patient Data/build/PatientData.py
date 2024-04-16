import mysql.connector
from datetime import datetime
import re

def update_session_active_data(id, new_session):
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

        # SQL query to update the "current_session" column in the "session_active" table
        update_query = """
        UPDATE session_active
        SET current_session = %s
        WHERE id = %s
        """

        # Data for update
        data = (new_session, id)

        # Executing the SQL query with data
        cursor.execute(update_query, data)

        # Committing the changes
        connection.commit()

        # print("Data updated successfully!")

    except mysql.connector.Error as error:
        print("Error updating data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def get_date_by_details(pt, firstname, lastname, session_number):
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

        # SQL query to select the "date" value based on the provided details
        select_query = """
        SELECT date
        FROM session_details
        WHERE pt = %s AND firstname = %s AND lastname = %s AND session_number = %s
        """

        # Executing the SQL query with parameters
        cursor.execute(select_query, (pt, firstname, lastname, session_number))

        # Fetching the result
        result = cursor.fetchone()

        if result:
            date_value = result[0]
            return date_value
            # print("Date value:", date_value)
        else:
            print("No data found for the provided details.")

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


edata = extract_patient_data_by_id(1)
# if data:
#     print(data)  # Output: ["pt", "firstname", "lastname"]
# print(edata)

# Example usage:
result = extract_columns_from_patient_details(edata[0], edata[1], edata[2])

srtn = ""
latest_session_number2 = "-"
latest_session_number = "-"
output_date = "-"
output_date2 = "-"

latest_session_number = get_latest_session_details(edata[0], edata[1], edata[2])
if(latest_session_number == None):
    latest_session_number = "-"
    output_date = "-"
    output_date2 = "-"

else:

    # Regular expression pattern to separate letters and numbers
    pattern = r'([A-Za-z]+)(\d+)'

    # Find the match of letters and numbers in the string
    matches = re.match(pattern, latest_session_number)

    if matches:
        # Extract letters and numbers from the match
        letters = matches.group(1)
        numbers = matches.group(2)
        
        # # Print the letters and numbers found
        # print("Letters:", letters)
        # print("Numbers:", numbers)
        new_num = int(numbers) - 1
        if(new_num <= 0):
            output_date2 = "-"
            latest_session_number2 = "-"

        else:
            session_str = "Session" + str(new_num)
            latest_session_number2 = session_str
            srtn2 = get_date_by_details(edata[0], edata[1], edata[2], latest_session_number2)

            parsed_date2 = datetime.strptime(srtn2, "%Y-%m-%d")

            # Format the datetime object to the desired format
            output_date2 = parsed_date2.strftime("%B %d, %Y")


    srtn = get_date_by_details(edata[0], edata[1], edata[2], latest_session_number)

    parsed_date = datetime.strptime(srtn, "%Y-%m-%d")

    # Format the datetime object to the desired format
    output_date = parsed_date.strftime("%B %d, %Y")

# print(result) # age, startoftherapy, totalsession, physician

# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

def view1():
    # print(latest_session_number2)
    update_session_active_data(1, latest_session_number2)
    window.destroy()

def view2():
    # print(latest_session_number)
    update_session_active_data(1, latest_session_number)
    window.destroy()



from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"D:\GRIP Despro\Patient Data\build\assets\frame0")

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
    x=703.0,
    y=535.0,
    width=146.0,
    height=36.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_2 clicked"), window.destroy()],
    relief="flat"
)
button_2.place(
    x=541.0,
    y=535.0,
    width=146.0,
    height=36.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_3 clicked"), window.destroy()],
    relief="flat"
)
button_3.place(
    x=372.0,
    y=535.0,
    width=149.0,
    height=36.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_4 clicked"), view1()],
    relief="flat"
)
button_4.place(
    x=418.0341796875,
    y=423.35400390625,
    width=139.25926208496094,
    height=35.03125
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_5 clicked"), view2()],
    relief="flat"
)
button_5.place(
    x=651.8466796875,
    y=423.35400390625,
    width=139.25926208496094,
    height=35.03125
)

canvas.create_text(
    407.0,
    393.0,
    anchor="nw",
    text=output_date2,
    fill="#FFFFFF",
    font=("Inter Medium", 15 * -1)
)

canvas.create_text(
    641.0,
    394.0,
    anchor="nw",
    text="  " + output_date,
    fill="#FFFFFF",
    font=("Inter Medium", 15 * -1)
)

canvas.create_text(
    679.0,
    369.0,
    anchor="nw",
    text=latest_session_number,
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_text(
    448.0,
    364.0,
    anchor="nw",
    text=latest_session_number2,
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
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

# canvas.create_text(
#     60.0,
#     59.0,
#     anchor="nw",
#     text="Juan",
#     fill="#FFFFFF",
#     font=("Inter Bold", 40 * -1)
# )

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_6 clicked"), window.destroy()],
    relief="flat"
)
button_6.place(
    x=676.0,
    y=138.0,
    width=144.0,
    height=39.0
)
window.resizable(False, False)
window.mainloop()
