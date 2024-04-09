from pathlib import Path
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def main():
    window = tk.Tk()
    window.geometry("900x600")
    window.geometry("+10+10")
    window.configure(bg="#FFFFFF")

    canvas = tk.Canvas(
        window,
        bg="#FFFFFF",
        height=600,
        width=900,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(450.0, 300.0, image=image_image_1)

    button_image_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = tk.Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [print("button_1 clicked"), window.destroy()],
        relief="flat"
    )
    button_1.place(x=677.0, y=131.0, width=139.25926208496094, height=37.03125)

    button_image_2 = tk.PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = tk.Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [print("button_2 clicked"), window.destroy()],
        relief="flat"
    )
    button_2.place(x=532.0, y=133.0, width=139.25926208496094, height=37.0)

    # Inserting Table
    table = Table(window, width=680)
    table.place(x=100, y=200)

    window.bind("<Configure>", lambda e: table.resize())

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

        self.create_table()

    def on_row_click(self, event):
     
        row = event.widget.grid_info()["row"]
        first_name = self.data[row - 1][0]
        last_name = self.data[row - 1][1]
        print("Clicked row:", row)
        print("First Name:", first_name)
        print("Last Name:", last_name)
        self.master.destroy()

    def create_table(self):
        headers = ['Firstname', 'Lastname', 'Last Session', 'Status']
        self.data = [
            ['John', 'Doe', 'Session 1', 'Active'],
            ['Jane', 'Smith', 'Session 2', 'Inactive'],
            ['Alice', 'Johnson', 'Session 3', 'Active'],
            ['Bob', 'Williams', 'Session 4', 'Active'],
            ['Emily', 'Brown', 'Session 5', 'Inactive'],
            ['Michael', 'Jones', 'Session 6', 'Active'],
            ['Emma', 'Garcia', 'Session 7', 'Inactive'],
            ['William', 'Martinez', 'Session 8', 'Active'],
            ['Sophia', 'Lee', 'Session 9', 'Active'],
            ['James', 'Taylor', 'Session 10', 'Inactive'],
            ['David', 'Miller', 'Session 11', 'Active'],
            ['Olivia', 'Wilson', 'Session 12', 'Inactive'],
            ['Liam', 'Moore', 'Session 13', 'Active'],
            ['Charlotte', 'Anderson', 'Session 14', 'Active'],
            ['Ethan', 'Thomas', 'Session 15', 'Inactive'],
            ['Isabella', 'Jackson', 'Session 16', 'Active'],
            ['Mason', 'White', 'Session 17', 'Inactive'],
            ['Ava', 'Harris', 'Session 18', 'Active'],
            ['Noah', 'Martin', 'Session 19', 'Active'],
            ['Sophie', 'Thompson', 'Session 20', 'Inactive']
        ]

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

    def resize(self):
        self.canvas.configure(width=self.fixed_width)  # Set canvas width to fixed width

        self.canvas.configure(height=340)  # Set canvas width to fixed width

        # self.canvas.configure(width=self.height)  # Set canvas width to fixed width
        self.scrollable_frame.update_idletasks()  # Update frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))  # Update scroll region

if __name__ == "__main__":
    main()
