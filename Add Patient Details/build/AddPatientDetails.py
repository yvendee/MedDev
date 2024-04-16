

import mysql.connector

import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import datetime

def show_calendar(root, event):
    def on_date_selected():
        selected_date = cal.get_date()
        entry_3.delete(0, tk.END)  # Clear the current entry value
        entry_3.insert(0, selected_date)  # Insert the selected date into the entry
        window.destroy()  # Close the calendar window after date selection

    # Create a new window
    window = tk.Toplevel(root)
    window.title("Calendar")

    # Create a Calendar widget
    cal = Calendar(window, selectmode='day', year=2024, month=4, day=14)
    cal.pack(padx=20, pady=20)

    # Create a button to select the date
    select_btn = tk.Button(window, text="Select Date", command=on_date_selected)
    select_btn.pack(pady=10)

def show_error_dialog(msg):
    messagebox.showerror("Error", msg)

def show_success_dialog(msg):
    messagebox.showinfo("Success", msg)


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
        show_error_dialog("Error fetching data")

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    return pt_info


def insert_patient_details(pt, firstname, lastname, age, startoftherapy):
    try:

        status = "Inactive"
        lastsession = "-"
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
            # print("Duplicate entry for patient:", firstname, lastname)
            show_error_dialog("Duplicate entry for patient!")
            return False

        # SQL query to insert new data into the "patient_details" table
        insert_query = """
        INSERT INTO patient_details (pt, firstname, lastname, age, startoftherapy, status, lastsession)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Data to be inserted
        data = (pt, firstname, lastname, age, startoftherapy, status, lastsession)

        # Executing the SQL query with data as parameters
        cursor.execute(insert_query, data)

        # Committing the changes
        connection.commit()
        show_success_dialog("Data inserted successfully!")
        return True

    except mysql.connector.Error as error:
        show_error_dialog("Error inserting data!")
        return False

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def test():
    mode = 0
    value = entry_1.get() ## lastname
    print("Current value of entry_1:", value)
    value2 = entry_2.get() ## firstname
    print("Current value of entry_2:", value2)
    value3 = entry_3.get() ## start of therapy
    print("Current value of entry_3:", value3)
    value4 = entry_4.get() ## age
    print("Current value of entry_4:", value4)

    # Example usage
    ptname_ptlastname = extract_ptname_ptlastname()
    print(ptname_ptlastname)

    pt = ptname_ptlastname[0] + ptname_ptlastname[1]


    value3 = "/".join(reversed(value3.split("/")))

    insert_successful = insert_patient_details(pt, value2, value, value4, value3)
    # if insert_successful:
    #     print("Data inserted successfully!")
    # else:
    #     print("Failed to insert data.")

    window.destroy()


# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"D:\GRIP Despro\Add Patient Details\build\assets\frame0")

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
    300.0,
    300.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    300.5,
    305.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#9CE9E4",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=132.0,
    y=289.0,
    width=337.0,
    height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    299.5,
    241.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#9CE9E4",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=131.0,
    y=225.0,
    width=337.0,
    height=30.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    301.5,
    427.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#9CE9E4",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=133.0,
    y=411.0,
    width=337.0,
    height=30.0
)

entry_3.bind("<Button-1>", lambda event: show_calendar(window, event))

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    300.5,
    363.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#9CE9E4",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=132.0,
    y=347.0,
    width=337.0,
    height=30.0
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
    y=467.0,
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
    x=130.0,
    y=467.0,
    width=167.51266479492188,
    height=37.0
)
window.resizable(False, False)
window.mainloop()
