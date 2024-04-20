import tkinter as tk
from tkinter import Canvas, Button, PhotoImage
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Global variables for data
x_data = [1, 2, 3, 4, 5]
y_data = [10, 20, 25, 30, 35]

# Define a function to plot the graph
def plot_graph():
    # Create a figure and plot the graph with the current data
    fig = Figure(figsize=(8, 6), dpi=100)  # Adjust figsize as needed
    plot = fig.add_subplot(111)
    plot.plot(x_data, y_data)
    plot.set_xlabel('X Label')
    plot.set_ylabel('Y Label')
    plot.set_title('Sample Graph')

    # Embed the graph into the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=200, y=200)  # Adjust the position as needed

# Function to update the data and refresh the graph
def update_data():
    # Update the data (for demonstration, randomize y_data)
    import random
    global y_data
    y_data = [random.randint(10, 50) for _ in range(len(x_data))]

    # Re-plot the graph with updated data
    plot_graph()

# Your existing Tkinter window code
window = tk.Tk()
window.title("Graph Window")

# Call plot_graph() initially to display the graph
plot_graph()

# Button to update the data and refresh the graph
update_button = Button(window, text="Update Data", command=update_data)
update_button.place(x=200, y=100)  # Adjust the position as needed

# Your existing UI elements

window.resizable(False, False)
window.mainloop()
