import mysql.connector


def update_role(role, new_ptname, new_status):
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

            # SQL query to update data in the "grip_active" table
            update_query = """
            UPDATE grip_active
            SET ptname = %s, status = %s
            WHERE role = %s
            """

            # Data for the update query
            data = (new_ptname, new_status, role)

            # Execute the SQL query
            cursor.execute(update_query, data)

            # Committing the changes
            connection.commit()

            print("Data updated successfully!")

    except mysql.connector.Error as error:
        print("Error updating data:", error)

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
    mode = 0
    value = entry_1.get()
    print("Current value of entry_1:", value)
    value2 = entry_2.get()
    print("Current value of entry_2:", value2)


    # if(value == value2):
    value3 = entry_3.get()
    print("Current value of entry_3:", value3)


    data = read_data()
    # print(data)

    for i in range(0,len(data)):
        # print(data[i][1])
        if(data[i][1] == value3):
            if(data[i][2] == value2):
                if(data[i][3] == value):
                    mode = 1
                    break

    if(mode == 1):
        # Example usage
        update_role("admin", value3, "active")
        window.destroy()
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
    highlightthickness=0
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
    command=lambda: [print("button_1 clicked"),login()],
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
window.resizable(False, False)
window.mainloop()
