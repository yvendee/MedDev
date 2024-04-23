import mysql.connector
from tkinter import messagebox
from time import sleep

def show_error_dialog(msg):
    messagebox.showerror("Error", msg)

def show_success_dialog(msg):
    messagebox.showinfo("Success", msg)


def update_record(role, ptname, ptlastname, status):
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

            # Update query
            update_query = """
            UPDATE grip_active 
            SET role=%s, ptname=%s, ptlastname=%s, status=%s
            LIMIT 1
            """

            # Execute the SQL query
            cursor.execute(update_query, (role, ptname, ptlastname, status))
            connection.commit()

            # print("Record updated successfully")

    except mysql.connector.Error as error:
        print("Error updating record:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

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


def login():

#     button_1 clicked
# Current value of entry_1: testx
# Current value of entry_2: worldx
# Current value of entry_3: hellox
# Data updated successfully!
    mode = 0
    value = entry_1.get()
    # print("Current value of entry_1:", value)
    value2 = entry_2.get()
    # print("Current value of entry_2:", value2)


    # if(value == value2):
    value3 = entry_3.get()
    # print("Current value of entry_3:", value3)##


    data = read_data()
    # print(data)

    for i in range(0,len(data)):
        # print(data[i][1])
        if(data[i][1] == value3):  ## firstname
            if(data[i][2] == value2): ##lastname
                if(data[i][3] == value): ## password
                    mode = 1
                    break




    if(mode == 1):
        # Example usage
        # print(data[i][0])
        update_record("Admin", value3, value2, str(data[i][0]))
        print("button_1 clicked")
        show_success_dialog("Account Accepted!")
        window.destroy()

    else:
        show_error_dialog("Wrong username or password!")
        
        # print("success")
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"D:\GRIP Despro\Log In\build\assets\frame0")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def on_close():
    print("exit")
    window.destroy()

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
    424.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#9CE9E4",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
entry_1.place(
    x=132.0,
    y=408.0,
    width=337.0,
    height=31.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    300.5,
    347.5,
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
    y=331.0,
    width=337.0,
    height=31.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    300.5,
    270.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#9CE9E4",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=132.0,
    y=254.0,
    width=337.0,
    height=31.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [login()],

    relief="flat"
)
button_1.place(
    x=314.0,
    y=468.21197509765625,
    width=165.0,
    height=37.92269515991211
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
    y=468.21197509765625,
    width=167.51266479492188,
    height=37.92269515991211
)
window.protocol("WM_DELETE_WINDOW", on_close)  # Handle window closing event
window.resizable(False, False)
window.mainloop()

