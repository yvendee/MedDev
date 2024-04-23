import mysql.connector

def update_patient_data(new_pt, new_firstname, new_lastname, id_value):
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

        # SQL query to update the data in the "patient_active" table
        update_query = """
        UPDATE patient_active
        SET pt = %s, firstname = %s, lastname = %s
        WHERE id = %s
        """
        # Data to be updated
        data = (new_pt, new_firstname, new_lastname, id_value)

        # Execute the SQL query
        cursor.execute(update_query, data)

        # Commit the changes
        connection.commit()

        # print("Data updated successfully")

    except mysql.connector.Error as error:
        print("Error updating data:", error)

    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            
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


def extract_data2(pt_value, firstname):
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

        # SQL query to fetch required columns from the table based on the 'pt' value and 'firstname'
        select_query = """
        SELECT firstname, lastname, lastsession, status 
        FROM patient_details 
        WHERE pt = %s AND firstname = %s
        """

        # Executing the SQL query with the specified 'pt' value and 'firstname'
        cursor.execute(select_query, (pt_value, firstname))

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

ptname_ptlastname = extract_ptname_ptlastname()
pt_value = ptname_ptlastname[0] + ptname_ptlastname[1]

# Extract the required data
extracted_data = extract_data(pt_value)

# Print the extracted data
mylist = []
for row in extracted_data:
    mylist.append(row)

# print(mylist)

from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

##new
def main():
    global mylist
    global entry_1
    global table
    global window
    # window = Tk()
    window = tk.Tk()

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
        command=lambda: [print("button_2 clicked"),window.destroy()], ##add
        relief="flat"
    )
    button_1.place(
        x=428.0,
        y=115.0,
        width=139.25926208496094,
        height=37.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [print("button_3 clicked"),window.destroy()],## back
        # command=lambda: [print("button_3 clicked"),window.destroy()], ## back
        relief="flat"
    )
    button_2.place(
        x=63.0,
        y=120.0,
        width=66.0,
        height=37.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        # command=lambda: [print("button_1 clicked"), window.destroy()], #search
        # command=lambda: [print("button_2 clicked"), window.destroy()],
        command=lambda: [search()], #search
        relief="flat"
    )
    button_3.place(
        x=790.0,
        y=115.0,
        width=46.0,
        height=37.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        691.0,
        133.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#9CE9E4",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=592.0,
        y=121.0,
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


# def main():
#     global mylist
#     window = tk.Tk()
#     window.geometry("900x600")
#     window.geometry("+10+10")
#     window.configure(bg="#FFFFFF")

#     canvas = tk.Canvas(
#         window,
#         bg="#FFFFFF",
#         height=600,
#         width=900,
#         bd=0,
#         highlightthickness=0,
#         relief="ridge"
#     )
#     canvas.place(x=0, y=0)

#     image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
#     image_1 = canvas.create_image(450.0, 300.0, image=image_image_1)

#     button_image_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
#     button_1 = tk.Button(
#         image=button_image_1,
#         borderwidth=0,
#         highlightthickness=0,
#         # command=lambda: [print("button_1 clicked"), window.destroy()],
#         command=lambda: [print("button_1 clicked")],
#         relief="flat"
#     )
#     button_1.place(x=677.0, y=131.0, width=139.25926208496094, height=37.03125)

#     button_image_2 = tk.PhotoImage(file=relative_to_assets("button_2.png"))
#     button_2 = tk.Button(
#         image=button_image_2,
#         borderwidth=0,
#         highlightthickness=0,
#         # command=lambda: [print("button_2 clicked"), window.destroy()],
#         command=lambda: [print("button_2 clicked")],
#         relief="flat"
#     )
#     button_2.place(x=532.0, y=133.0, width=139.25926208496094, height=37.0)

#     # Inserting Table
#     table = Table(window, width=680)
#     table.place(x=100, y=200)

#     window.bind("<Configure>", lambda e: table.resize())

#     window.resizable(False, False)
#     window.mainloop()

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

        self.create_table(mylist)

    def on_row_click(self, event):
     
        row = event.widget.grid_info()["row"]
        first_name = self.data[row - 1][0]
        last_name = self.data[row - 1][1]
        print("Clicked row:", row)
        # print("First Name:", first_name)
        # print("Last Name:", last_name)

        ptname_ptlastname = extract_ptname_ptlastname()
        # print(ptname_ptlastname)
        pt_value = ptname_ptlastname[0] + ptname_ptlastname[1]
        
        update_patient_data(pt_value, first_name, last_name, 1)

        self.master.destroy()

    def create_table(self, data):
        headers = ['Firstname', 'Lastname', 'Last Session', 'Status']
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
            header_label = tk.Label(self.scrollable_frame, text=header, font=('Arial', 20, 'bold'))
            header_label.grid(row=0, column=col, padx=10, pady=5)

        # Create data rows
        for row, entry in enumerate(self.data, start=1):
            for col, value in enumerate(entry):
                data_label = tk.Label(self.scrollable_frame, text=value, font=('Arial', 20))
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

    ptname_ptlastname = extract_ptname_ptlastname()
    pt_value = ptname_ptlastname[0] + ptname_ptlastname[1]

    # Extract the required data
    extracted_data = extract_data2(pt_value,entry_value)
    # print(extracted_data)

    # Update the table with new data
    table.update_data(extracted_data)

def on_close():
    print("exit")
    window.destroy()

if __name__ == "__main__":
    main()
