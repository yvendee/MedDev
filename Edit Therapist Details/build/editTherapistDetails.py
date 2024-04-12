import mysql.connector


user_id = 0


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

            print("Record updated successfully")

    except mysql.connector.Error as error:
        print("Error updating record:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()



def extract_status():
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

        # SQL query to select status value from the grip_active table
        select_query = """
        SELECT status FROM grip_active LIMIT 1
        """

        # Executing the SQL query
        cursor.execute(select_query)

        # Fetching the status value
        status_value = cursor.fetchone()

        if status_value:
            return int(status_value[0])
        else:
            print("No status value found in the grip_active table")
            return None

    except mysql.connector.Error as error:
        print("Error:", error)
        return None

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()



def update_user_info(user_id, new_firstname, new_lastname, new_password):
    try:
        # Establishing the connection to MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gripdespro"
        )

        if not connection.is_connected():
            print("Connection failed")
            return False

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to update firstname, lastname, and password based on id
        update_query = """
        UPDATE grip_signup
        SET firstname = %s, lastname = %s, password = %s
        WHERE id = %s
        """

        # Executing the SQL query with new values and user_id as parameters
        cursor.execute(update_query, (new_firstname, new_lastname, new_password, user_id))

        # Committing the changes
        connection.commit()

        # print("User information updated successfully!")
        return True

    except mysql.connector.Error as error:
        print("Error:", error)
        return False

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()



def test():
    global user_id

    value = entry_1.get()
    # print("Current value of entry_1:", value)
    value2 = entry_2.get()
    # print("Current value of entry_2:", value2)

    if(value == value2):
        value3 = entry_3.get()
        # print("Current value of entry_3:", value3)
        value4 = entry_4.get()
        # print("Current value of entry_4:", value4)


        update_successful = update_user_info(user_id, value4, value3, value2)
        if update_successful:
            update_record("admin", value4, value3, user_id)
            # print("User information updated successfully!")
            window.destroy()
        # else:
        #     print("Failed to update user information.")




def get_name_by_id(user_id):
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

        # SQL query to select firstname and lastname based on id
        select_query = """
        SELECT firstname, lastname FROM grip_signup WHERE id = %s
        """

        # Executing the SQL query with user_id as parameter
        cursor.execute(select_query, (user_id,))

        # Fetching the result
        result = cursor.fetchone()

        if result:
            firstname, lastname = result
            return [firstname, lastname]
        else:
            return None

    except mysql.connector.Error as error:
        print(f"Error: {error}")
        return None

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()


# Example usage
user_id = extract_status()
# print("Status:", user_id)


name_list = get_name_by_id(user_id)
# print(name_list)  # Output the list containing firstname and lastname




# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer





from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"D:\GRIP Despro\Edit Therapist Details\build\assets\frame0")

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
    295.5,
    448.0,
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
    x=127.0,
    y=432.0,
    width=337.0,
    height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    295.5,
    373.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#9CE9E4",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
entry_2.place(
    x=127.0,
    y=357.0,
    width=337.0,
    height=30.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    295.5,
    296.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#9CE9E4",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=127.0,
    y=280.0,
    width=337.0,
    height=30.0
)

entry_3.delete(0, 'end')  # Clear existing text
entry_3.insert(0, name_list[1])  # Insert new text

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    295.5,
    221.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#9CE9E4",
    fg="#000716",
    highlightthickness=0,

)
entry_4.place(
    x=127.0,
    y=205.0,
    width=337.0,
    height=30.0
)

entry_4.delete(0, 'end')  # Clear existing text
entry_4.insert(0, name_list[0])  # Insert new text

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    # command=lambda: [print("button_1 clicked"),window.destroy()],
    command=lambda: [print("button_1 clicked"),test()],
    relief="flat"
)
button_1.place(
    x=130.0,
    y=502.0,
    width=170.0,
    height=37.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_2 clicked"),window.destroy()],
    # command=lambda: [print("button_2 clicked"),test()],
    relief="flat"
)
button_2.place(
    x=316.0,
    y=502.0,
    width=158.0,
    height=37.0
)
window.resizable(False, False)
window.mainloop()
