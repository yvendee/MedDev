

import mysql.connector

def extract_data(pt, firstname, lastname):
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

        # SQL query to fetch data for the specified columns and filter by pt, firstname, and lastname
        select_query = """
        SELECT date, hand, f1, f2, f3, f4, f5, remarks
        FROM archive_session
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Executing the SQL query with parameters
        cursor.execute(select_query, (pt, firstname, lastname))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Creating a list to store extracted data
        data = []

        # Iterating over the rows and appending the required columns to the data list
        for row in rows:
            data.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])

        return data

    except mysql.connector.Error as error:
        print("Error extracting data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def extract_data2(pt, firstname, lastname, date):
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

        # SQL query to fetch data for the specified columns and filter by pt, firstname, lastname, and date
        select_query = """
        SELECT date, hand, f1, f2, f3, f4, f5
        FROM archive_session
        WHERE pt = %s AND firstname = %s AND lastname = %s AND date = %s
        """

        # Executing the SQL query with parameters
        cursor.execute(select_query, (pt, firstname, lastname, date))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Creating a list to store extracted data
        data = []

        # Iterating over the rows and appending the required columns to the data list
        for row in rows:
            data.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])

        return data

    except mysql.connector.Error as error:
        print("Error extracting data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
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

mydata = extract_data(edata[0], edata[1], edata[2])

pt_str = edata[1] + " " + edata[2]
# Example usage:
result = extract_columns_from_patient_details(edata[0], edata[1], edata[2])
# print(result) # age, startoftherapy, totalsession, physician


# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def main():
    global mydata
    global entry_1
    global table
    global window

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
        59.0,
        52.0,
        anchor="nw",
        text=pt_str,
        fill="#FFFFFF",
        font=("Inter Bold", 35 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [search()],
        relief="flat"
    )
    button_1.place(
        x=786.0,
        y=129.0,
        width=46.0,
        height=37.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [print("button_2 clicked"),window.destroy()],
        relief="flat"
    )
    button_2.place(
        x=488.0,
        y=129.0,
        width=66.0,
        height=37.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        687.0,
        147.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#9CE9E4",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=588.0,
        y=135.0,
        width=198.0,
        height=22.0
    )

    # Inserting Table
    table = Table(window, width=680)
    table.place(x=100, y=200)

    window.bind("<Configure>", lambda e: table.resize())
    window.protocol("WM_DELETE_WINDOW", on_close)  # Handle window closing event

    window.resizable(False, False)
    window.mainloop()


class Table(tk.Frame):
    def __init__(self, master=None, height=400, **kwargs):
        super().__init__(master, **kwargs)
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.height = height
        self.fixed_width = kwargs.get('width', 1000)  # Fixed width parameter

        self.create_table(mydata)

    def on_row_click(self, event):
     
        row = event.widget.grid_info()["row"]
        # first_name = self.data[row - 1][0]
        # last_name = self.data[row - 1][1]
        print("Clicked row:", row)
        # # print("First Name:", first_name)
        # # print("Last Name:", last_name)

        # ptname_ptlastname = extract_ptname_ptlastname()
        # # print(ptname_ptlastname)
        # pt_value = ptname_ptlastname[0] + ptname_ptlastname[1]

        self.master.destroy()

    def create_table(self, data):
        headers = ['Date', 'Hand', 'Thumb', 'Pointer' , 'Middle', 'Ring', 'Pinky', 'Remarks']
        self.data = data
        # self.data = [
        #     ['John', 'Doe', 'Session 1', 'Active'],
        #     ['Jane', 'Smith', 'Session 2', 'Inactive'],
        #     ['Alice', 'Johnson', 'Session 3', 'Active'],
        #     ['Bob', 'Williams', 'Session 4', 'Active'],
        #     ['Emily', 'Brown', 'Session 5', 'Inactive'],
        #     ['Michael', 'Jones', 'Session 6', 'Active'],
        #     ['Emma', 'Garcia', 'Session 7', 'Inactive'],
        #     ['William', 'Martinez', 'Session 8', 'Active'],
        #     ['Sophia', 'Lee', 'Session 9', 'Active'],
        #     ['James', 'Taylor', 'Session 10', 'Inactive'],
        #     ['David', 'Miller', 'Session 11', 'Active'],
        #     ['Olivia', 'Wilson', 'Session 12', 'Inactive'],
        #     ['Liam', 'Moore', 'Session 13', 'Active'],
        #     ['Charlotte', 'Anderson', 'Session 14', 'Active'],
        #     ['Ethan', 'Thomas', 'Session 15', 'Inactive'],
        #     ['Isabella', 'Jackson', 'Session 16', 'Active'],
        #     ['Mason', 'White', 'Session 17', 'Inactive'],
        #     ['Ava', 'Harris', 'Session 18', 'Active'],
        #     ['Noah', 'Martin', 'Session 19', 'Active'],
        #     ['Sophie', 'Thompson', 'Session 20', 'Inactive']
        # ]

        # Create headers
        for col, header in enumerate(headers):
            header_label = tk.Label(self.scrollable_frame, text=header, font=('Arial', 12, 'bold'))
            header_label.grid(row=0, column=col, padx=10, pady=5)

        # Create data rows
        for row, entry in enumerate(self.data, start=1):
            for col, value in enumerate(entry):
                data_label = tk.Label(self.scrollable_frame, text=value, font=('Arial', 12))
                data_label.grid(row=row, column=col, padx=10, pady=5)
                data_label.bind("<Button-1>", self.on_row_click)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def update_data(self, new_data):
        self.data = new_data
        # Clear current table display
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        # Recreate the table with updated data
        self.create_table(new_data)

    def resize(self):
        self.canvas.configure(width=self.fixed_width)  # Set canvas width to fixed width

        self.canvas.configure(height=340)  # Set canvas width to fixed width

        # self.canvas.configure(width=self.height)  # Set canvas width to fixed width
        self.scrollable_frame.update_idletasks()  # Update frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))  # Update scroll region


def search():
    entry_value = entry_1.get()
    # Set initial text for entry_1
    entry_1.delete(0, "end")  # Clear the contents of entry_1

    edata = extract_patient_data_by_id(1)
    # if data:
    #     print(data)  # Output: ["pt", "firstname", "lastname"]

    extracted_data = extract_data2(edata[0], edata[1], edata[2], entry_value)
    # print(extracted_data)

    # Update the table with new data
    table.update_data(extracted_data)

def on_close():
    print("exit")
    window.destroy()

if __name__ == "__main__":
    main()