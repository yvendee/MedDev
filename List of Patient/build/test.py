import tkinter as tk

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

        self.create_table()

    def on_row_click(self, event):
        row = event.widget.grid_info()["row"]
        first_name = self.data[row - 1][0]
        last_name = self.data[row - 1][1]
        print("Clicked row:", row)
        print("First Name:", first_name)
        print("Last Name:", last_name)

    def create_table(self):
        headers = ['Firstname', 'Lastname', 'Session', 'Status']
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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Table Example")
    table = Table(root, height=400)
    table.pack(padx=10, pady=10, fill="both", expand=True)
    root.mainloop()
