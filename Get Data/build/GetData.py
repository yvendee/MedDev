import sys
import os
from time import sleep
import serial
import ast

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



from tkinter import messagebox

def show_error_dialog(msg):
    messagebox.showerror("Error", msg)

def show_success_dialog(msg):
    messagebox.showinfo("Success", msg)




def get_csvlist(__fullpath):
    try:
        with open(__fullpath, "r+", encoding='UTF-8') as __f:
            __list = list(__f)
            __f.close()
            __converted_list = []
            __item_count = 0
            for __i in __list:
                __converted_list.append(__i.strip())
                __item_count += 1
            #print('total lines: ' + str(__item_count))
            return __converted_list
    except Exception as e:
        print(e)
        return []

def Init_Genie(__port, __baudrate):
    global ser1
    try:
    #initializing hardware serial of arduino
        ser1 = serial.Serial(port = __port, baudrate = __baudrate,timeout = 0, writeTimeout=0)
        # print("[+] INFO Connected: " + __port + " at " + __baudrate + "bps")
        return True
    except Exception as e:
        print(e)
        print("[+] ERROR Comport failed!")
        return False

def genie_SendString(string):
    bytes_object = bytes(string, 'utf-8')
    ser1.write(bytes_object)



def Genie():

    line = []
    genie_SendString("1")
    rtn = ""
    while True:
        
        # Read a line from serial
        data = ser1.readline()
        
        # Append the line to the list
        # line.append(data.decode().strip())
        
        sleep(1)
        # print("wait")
        drtn = data.decode().strip()
        if(drtn == ""):
            pass
        else:
            # print(rtn)
            # print(len(rtn))
            rtn = drtn
            break
    return rtn




# print("Welcome!")
__listlist = []
__list = get_csvlist("config.txt")
for __i in range(0, len(__list)):
    __split = __list[__i].split("=")
    __listlist.append(__split)

__comport = ""
__baudrate = ""

__scount = 0
for __i in range(0, len(__listlist)):
    if(__listlist[__i][0] == "comport"):
        __comport = __listlist[__i][1]
        __scount += 1
    if(__listlist[__i][0] == "baudrate"):
        __baudrate = __listlist[__i][1]
        __scount += 1

if(__scount == 2):
    # print("[+] INFO config.txt loaded")
    pass
else:
    show_error_dialog("[+] ERROR config.txt")
    sys.exit()


if(Init_Genie(__comport, __baudrate)):
    pass

else:
    show_error_dialog("Can't connect to com port")
    sys.exit()

import mysql.connector



import datetime

import re


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

def insert_mockup_data(pt, firstname, lastname, session_number, l1, l2, l3, l4, l5, r1, r2, r3, r4, r5, date):
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

        # SQL query to insert mockup data into the session_details table
        insert_query = """
        INSERT INTO session_details (pt, firstname, lastname, session_number, l1, l2, l3, l4, l5, r1, r2, r3, r4, r5, date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Executing the SQL query
        cursor.execute(insert_query, (pt, firstname, lastname, session_number, l1, l2, l3, l4, l5, r1, r2, r3, r4, r5, date))

        # Committing the changes to the database
        connection.commit()

        # print("Mockup data inserted successfully!")

    except mysql.connector.Error as error:
        print("Error inserting mockup data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def insert_archive_session_data(pt, firstname, lastname, date, hand, f1, f2, f3, f4, f5):
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

        # SQL query to insert data into the "archive_session" table
        insert_query = """
        INSERT INTO archive_session (pt, firstname, lastname, date, hand, f1, f2, f3, f4, f5) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Data to be inserted
        data = (pt, firstname, lastname, date, hand, f1, f2, f3, f4, f5)

        # Executing the SQL query
        cursor.execute(insert_query, data)

        # Committing the changes to the database
        connection.commit()

        # print("Data inserted successfully!")

    except mysql.connector.Error as error:
        print("Error inserting data:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def update_totalsession(pt, firstname, lastname, new_total_session):
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

        # SQL query to update the "totalsession" column based on "pt", "firstname", and "lastname"
        update_query = """
        UPDATE patient_details 
        SET totalsession = %s 
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Data to be updated
        data = (new_total_session, pt, firstname, lastname)

        # Executing the SQL query
        cursor.execute(update_query, data)

        # Committing the changes to the database
        connection.commit()

        # print("Total session updated successfully!")

    except mysql.connector.Error as error:
        print("Error updating total session:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def count_entries(pt, firstname, lastname):
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
            return "Connection failed"

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL query to count the entries based on "pt", "firstname", and "lastname"
        count_query = """
        SELECT COUNT(*) 
        FROM archive_session 
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Data for the query
        data = (pt, firstname, lastname)

        # Executing the SQL query
        cursor.execute(count_query, data)

        # Fetching the count result
        count_result = cursor.fetchone()[0]

        return count_result

    except mysql.connector.Error as error:
        return f"Error counting entries: {error}"

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

def update_status(pt, firstname, lastname, status):
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

        # SQL query to update the "status" column based on "pt", "firstname", and "lastname"
        update_query = """
        UPDATE patient_details 
        SET status = %s 
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Data to be updated
        data = (status, pt, firstname, lastname)

        # Executing the SQL query
        cursor.execute(update_query, data)

        # Committing the changes to the database
        connection.commit()

        # print("Status updated successfully!")

    except mysql.connector.Error as error:
        print("Error updating status:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def update_last_session(pt, firstname, lastname, lastsession):
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

        # SQL query to update the "lastsession" column based on "pt", "firstname", and "lastname"
        update_query = """
        UPDATE patient_details 
        SET lastsession = %s 
        WHERE pt = %s AND firstname = %s AND lastname = %s
        """

        # Data to be updated
        data = (lastsession, pt, firstname, lastname)

        # Executing the SQL query
        cursor.execute(update_query, data)

        # Committing the changes to the database
        connection.commit()

        # print("Last session updated successfully!")

    except mysql.connector.Error as error:
        print("Error updating last session:", error)

    finally:
        # Closing the cursor
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()


# Sample data for plotting
x_data = [1, 2, 3, 4, 5]
y_data = [0, 0, 0, 0, 0]

# Define a function to plot the graph
def plot_graph():
    global x_data, y_data

    # Create a figure and plot the graph
    fig = Figure(figsize=(4, 3), dpi=100)
    plot = fig.add_subplot(111)
    plot.plot(x_data, y_data)
    # plot.set_xlabel('X Label')
    # plot.set_ylabel('Y Label')
    plot.set_title('Flex Sensor Data')

    # Embed the graph into the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=450, y=137)  # Adjust the position as needed


mode = "left"

leftlist =  ["0","0","0","0","0"]
rightlist = ["0","0","0","0","0"]
showlist = ["0","0","0","0","0"]


# leftlist =  ["1","2","3","4","5"]
# rightlist = ["6","7","8","9","10"]

# leftlist =  ["10","20","30","40","50"]
# rightlist = ["60","70","80","90","10"]

def sendmsg(cmd_str):
    global mode, rightlist, leftlist, y_data

    x = Genie()

    try:
        # Attempt to convert the received string to a list
        converted_list = ast.literal_eval(x)

        # Initialize an empty list to store the processed integers
        processed_items = []

        # Convert each item to int, taking absolute value to ensure positivity
        for item in converted_list:
            item = item.strip()
            processed_items.append(abs(int(item.strip())))

        # Print the converted list for debugging
        # print(processed_items)
        # print(type(processed_items))


        y_data = processed_items
        plot_graph()

        max_number = max(map(int, processed_items))
        # print(cmd_str)
        # print(max_number)


        # Depending on the mode, assign the converted list to the appropriate variable
        if mode == "left":
            if(cmd_str == "thumbPress"):
                leftlist[0] = max_number;
                canvas.itemconfig(text_object1, text=leftlist[0])
            elif(cmd_str == "pointerPress"):
                leftlist[1] = max_number;
                canvas.itemconfig(text_object2, text=leftlist[1])
            elif(cmd_str == "middlePress"):
                leftlist[2] = max_number;
                canvas.itemconfig(text_object3, text=leftlist[2])
            elif(cmd_str == "ringPress"):
                leftlist[3] = max_number;
                canvas.itemconfig(text_object4, text=leftlist[3])
            elif(cmd_str == "pinkyPress"):
                leftlist[4] = max_number;
                canvas.itemconfig(text_object5, text=leftlist[4])

            # leftlist = processed_items
        elif mode == "right":

            if(cmd_str == "thumbPress"):
                rightlist[0] = max_number;
                canvas.itemconfig(text_object1, text=rightlist[0])
            elif(cmd_str == "pointerPress"):
                rightlist[1] = max_number;
                canvas.itemconfig(text_object2, text=rightlist[1])
            elif(cmd_str == "middlePress"):
                rightlist[2] = max_number;
                canvas.itemconfig(text_object3, text=rightlist[2])
            elif(cmd_str == "ringPress"):
                rightlist[3] = max_number;
                canvas.itemconfig(text_object4, text=rightlist[3])
            elif(cmd_str == "pinkyPress"):
                rightlist[4] = max_number;
                canvas.itemconfig(text_object5, text=rightlist[4])
            # rightlist = processed_items

        # Show success dialog
        show_success_dialog("Success: " + str(processed_items))

        # Optionally, plot the graph here

    except Exception as e:
        # If an exception occurs during conversion or assignment, show error dialog
        show_error_dialog("Improper format from serial: " + str(e))



def backtomenu():
    # update_data()

    window.destroy()




def confirm():

    global mode, leftlist, rightlist

    # Get the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    data = extract_patient_data_by_id(1)
    # if data:
    #     print(data)  # Output: ["pt", "firstname", "lastname"]

    uppercase_string = mode[0].upper() + mode[1:]

    if(mode == "right"):
        f1 = rightlist[0]
        f2 = rightlist[1]
        f3 = rightlist[2]
        f4 = rightlist[3]
        f5 = rightlist[4]

    else:

        f1 = leftlist[0]
        f2 = leftlist[1]
        f3 = leftlist[2]
        f4 = leftlist[3]
        f5 = leftlist[4]

    # Insert data into the "archive_session" table
    # insert_archive_session_data(pt, firstname, lastname, date, hand, f1, f2, f3, f4, f5)
    
    insert_archive_session_data(data[0], data[1], data[2], current_date, uppercase_string, f1, f2, f3, f4, f5)


    # Update the "lastsession" column in the "patient_details" table
    update_last_session(data[0], data[1], data[2], current_date)

    update_status(data[0], data[1], data[2], "Active")

    scount = count_entries(edata[0], edata[1], edata[2])
    # print(scount)


    update_totalsession(data[0], data[1], data[2], scount)

    show_success_dialog("Success")


    ###############################################################################

    # Get the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    data = extract_patient_data_by_id(1)

    # Get the latest session number for the given pt, firstname, and lastname
    latest_session_number = get_latest_session_details(data[0], data[1], data[2])

    # print("Latest Session Number:", latest_session_number)

    if(latest_session_number == None):
        # print("not found!")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        # Example usage: Insert mockup data into the session_details table
        insert_mockup_data(data[0], data[1], data[2], "Session1", leftlist[0], leftlist[1], leftlist[2], leftlist[3], leftlist[4], rightlist[0], rightlist[1], rightlist[2], rightlist[3], rightlist[4], current_date)

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
            new_num = int(numbers) + 1
            session_str = "Session" + str(new_num)

            insert_mockup_data(data[0], data[1], data[2], session_str, leftlist[0], leftlist[1], leftlist[2], leftlist[3], leftlist[4], rightlist[0], rightlist[1], rightlist[2], rightlist[3], rightlist[4], current_date)
    

    # window.destroy()


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

# Example usage:
result = extract_columns_from_patient_details(edata[0], edata[1], edata[2])
# print(result) # age, startoftherapy, totalsession, physician


# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"D:\GRIP Despro\Get Data\build\assets\frame0")


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("900x600")
window.configure(bg = "#FFFFFF")

def change_button(button, new_image):
        button.config(image=new_image)
        
        
def leftPress():
    global mode
    # Change button image to a new image
    change_button(left, leftpress)
    change_button(right, right_btn_image)
    # print("leftPress")
    mode = "left"

leftpress = PhotoImage(file=relative_to_assets("leftpress.png"))

def rightPress():
    global mode
    # Change button image to a new image
    change_button(right, rightpress)
    change_button(left, left_btn_image)
    # print("rightPress")
    mode = "right"

rightpress = PhotoImage(file=relative_to_assets("rightpress.png"))

def thumbPress():
    # Change button image to a new image
    change_button(thumb, thumbpress)
    change_button(pointer, pointer_btn_image)
    change_button(pinky, pinky_btn_image)
    change_button(middle, middle_btn_image)
    change_button(ring, ring_btn_image)
    sendmsg("thumbPress")

thumbpress = PhotoImage(file=relative_to_assets("thumbpress.png"))

def pointerPress():
    # Change button image to a new image
    change_button(pointer, pointerpress)
    change_button(thumb, thumb_btn_image)
    change_button(pinky, pinky_btn_image)
    change_button(middle, middle_btn_image)
    change_button(ring, ring_btn_image)
    sendmsg("pointerPress")
 
pointerpress = PhotoImage(file=relative_to_assets("pointerpress.png"))

def middlePress():
    # Change button image to a new image
    change_button(middle, middlepress)
    change_button(thumb, thumb_btn_image)
    change_button(pinky, pinky_btn_image)
    change_button(pointer, pointer_btn_image)
    change_button(ring, ring_btn_image)
    sendmsg("middlePress")

middlepress = PhotoImage(file=relative_to_assets("middlepress.png"))

def ringPress():
    # Change button image to a new image
    change_button(ring, ringpress)
    change_button(thumb, thumb_btn_image)
    change_button(pinky, pinky_btn_image)
    change_button(pointer, pointer_btn_image)
    change_button(middle, middle_btn_image)
    sendmsg("ringPress")

ringpress = PhotoImage(file=relative_to_assets("ringpress.png"))

def pinkyPress():
    # Change button image to a new image
    change_button(pinky, pinkypress)
    change_button(thumb, thumb_btn_image)
    change_button(pointer, pointer_btn_image)
    change_button(middle, middle_btn_image)
    change_button(ring, ring_btn_image)
    sendmsg("pinkyPress")

pinkypress = PhotoImage(file=relative_to_assets("pinkypress.png"))



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

left_btn_image = PhotoImage(
    file=relative_to_assets("left.png"))
left = Button(
    image=left_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=leftPress,
    relief="flat"
)
left.place(
    x=630.0,
    y=462.0,
    width=85.0,
    height=24.0
)

right_btn_image = PhotoImage(
    file=relative_to_assets("right.png"))
right = Button(
    image=right_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=rightPress,
    relief="flat"
)
right.place(
    x=736.0,
    y=462.0,
    width=85.0,
    height=24.0
)

thumb_btn_image = PhotoImage(
    file=relative_to_assets("thumb.png"))
thumb = Button(
    image=thumb_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=thumbPress,
    relief="flat"
)
thumb.place(
    x=338.0,
    y=154.0,
    width=90.0,
    height=25.0
)

pointer_btn_image = PhotoImage(
    file=relative_to_assets("pointer.png"))
pointer = Button(
    image=pointer_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=pointerPress,
    relief="flat"
)
pointer.place(
    x=338.0,
    y=214.0,
    width=90.173583984375,
    height=25.0
)

middle_btn_image = PhotoImage(
    file=relative_to_assets("middle.png"))
middle = Button(
    image=middle_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=middlePress,
    relief="flat"
)
middle.place(
    x=338.1739196777344,
    y=274.0,
    width=90.0,
    height=25.0
)

ring_btn_image = PhotoImage(
    file=relative_to_assets("ring.png"))
ring = Button(
    image=ring_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=ringPress,
    relief="flat"
)
ring.place(
    x=338.1739196777344,
    y=334.0,
    width=90.0,
    height=25.0
)

pinky_btn_image = PhotoImage(
    file=relative_to_assets("pinky.png"))
pinky = Button(
    image=pinky_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=pinkyPress,
    relief="flat"
)
pinky.place(
    x=338.1739196777344,
    y=394.0,
    width=90.0,
    height=25.0
)

canvas.create_text(
    51.0,
    27.0,
    anchor="nw",
    text=edata[1],
    fill="#FFFFFF",
    font=("Inter Bold", 40 * -1)
)

canvas.create_text(
    51.0,
    76.0,
    anchor="nw",
    text=edata[2],
    fill="#FFFFFF",
    font=("Inter Bold", 40 * -1)
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    # command=lambda: [print("button_8 clicked"), window.destroy()],
    command=lambda: [print("button_8 clicked"), confirm()], ## confimr
    relief="flat"
)
button_8.place(
    x=706.0,
    y=519.0,
    width=146.0,
    height=36.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_9 clicked"), backtomenu()], ## back to main menu
    relief="flat"
)
button_9.place(
    x=535.0,
    y=519.0,
    width=146.0,
    height=36.0
)

text_object1 = canvas.create_text(
    372.0,
    184.0,
    anchor="nw",
    text=showlist[0], ##thumb
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

text_object5 = canvas.create_text(
    374.0,
    424.0,
    anchor="nw",
    text=showlist[4], ## pinky
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

text_object4 = canvas.create_text(
    374.0,
    364.0,
    anchor="nw",
    text=showlist[3],   ## ring
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

text_object3 = canvas.create_text(
    374.0,
    304.0,
    anchor="nw",
    text=showlist[2],   ## middle
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

text_object2 = canvas.create_text(
    374.0,
    244.0,
    anchor="nw",
    text=showlist[1],   ## pointer
    fill="#000000",
    font=("Inter Bold", 10 * -1)
)

canvas.create_text(
    54.0,
    238.0,
    anchor="nw",
    text=result[1],
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_text(
    54.0,
    369.0,
    anchor="nw",
    text=edata[0],
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_text(
    54.0,
    184.0,
    anchor="nw",
    text=result[0],
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_text(
    54.0,
    295.0,
    anchor="nw",
    text=result[2],
    fill="#FFFFFF",
    font=("Inter Bold", 15 * -1)
)

canvas.create_text(  ##suggested
    485.0,
    465.0,
    anchor="nw",
    text="15 minutes",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)


plot_graph()
window.resizable(False, False)
window.mainloop()
