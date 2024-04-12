import mysql.connector


import mysql.connector

def update_age_startoftherapy(pt, firstname, lastname, new_age, new_startoftherapy):
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
            return False  # Return False if connection fails

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to update age and startoftherapy based on pt, firstname, and lastname
        update_query = """
        UPDATE patient_details
        SET age = %s, startoftherapy = %s
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Executing the SQL query with the provided parameters
        cursor.execute(update_query, (new_age, new_startoftherapy, pt, firstname, lastname))

        # Committing the changes
        connection.commit()

        # Check if any row was affected
        if cursor.rowcount > 0:
            print("Age and Start of Therapy updated successfully.")
            return True
        else:
            print("No matching record found.")
            return False

    except mysql.connector.Error as error:
        print("Error:", error)
        return False  # Return False if an error occurs

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def extract_age_startoftherapy(pt, firstname, lastname):
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
            return ["", ""]  # Return empty list if connection fails

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to select specific columns from the "patient_details" table based on pt, firstname, and lastname
        select_query = """
        SELECT age, startoftherapy
        FROM patient_details
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Executing the SQL query with the provided parameters
        cursor.execute(select_query, (pt, firstname, lastname))

        # Fetching the first row from the result
        row = cursor.fetchone()

        if row:
            age, startoftherapy = row
            return [age, startoftherapy]  # Return list with extracted data
        else:
            return ["", ""]  # Return empty list if no matching patient found

    except mysql.connector.Error as error:
        print("Error:", error)
        return ["", ""]  # Return empty list if error occurs

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


def test():

    value = entry_1.get()
    # print("Current value of entry_1:", value) ## age
    value2 = entry_2.get()
    # print("Current value of entry_2:", value2) ##startoftherapy
    edata = extract_patient_data_by_id(1)

    updated = update_age_startoftherapy(edata[0], edata[1], edata[2], value, value2)
    window.destroy()


    # # if(value == value2):
    # value3 = entry_3.get()
    # # print("Current value of entry_3:", value3)##

edata = extract_patient_data_by_id(1)

# Example usage:
result = extract_age_startoftherapy(edata[0], edata[1], edata[2])
# print(result)  # Output: ["", ""]

# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"D:\GRIP Despro\Edit Patient Details\build\assets\frame0")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("600x600")
window.geometry("+10+10") ## Kayven added x,y
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 600,
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

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    300.5,
    292.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#9CE9E4",
    fg="#000716",
    highlightthickness=0
)

entry_1.delete(0, 'end')  # Clear existing text
entry_1.insert(0, result[0])  # Insert new tex

entry_1.place(
    x=132.0,
    y=276.0,
    width=337.0,
    height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    300.5,
    390.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#9CE9E4",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=132.0,
    y=374.0,
    width=337.0,
    height=30.0
)

entry_2.delete(0, 'end')  # Clear existing text
entry_2.insert(0, result[1])  # Insert new tex

canvas.create_text(
    98.0,
    51.0,
    anchor="nw",
    text=edata[1],
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

canvas.create_text(
    98.0,
    87.0,
    anchor="nw",
    text=edata[2],
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    # command=lambda: [print("button_1 clicked"),window.destroy()],
    command=lambda: [print("button_1 clicked"), test()],
    relief="flat"
)
button_1.place(
    x=314.0,
    y=442.0,
    width=165.0,
    height=37.0
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
    x=122.0,
    y=442.0,
    width=167.51266479492188,
    height=37.0
)
window.resizable(False, False)
window.mainloop()
