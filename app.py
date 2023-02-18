# A Python GUI calulator built in Tkinter
# Lucas Bubner, 2023

# Required imports
import tkinter as tk

# Initialise new calculator container
class Calculator(tk.Tk):
    def __init__(self):
        # Run Tkinter initialisation
        super().__init__()

        # Configure display properties including title and grids
        self.title("Calculator")
        self.display = tk.Entry(self, width=33, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Change favicon
        self.iconphoto(False, tk.PhotoImage("./assets/icon.png"))

        # Prevent resizing
        self.resizable(False, False)

        # Create a Notebook widget for multiple tabs
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create the default tab
        self.basic_calculator = ttk.Frame(self.notebook)
        self.notebook.add(self.basic_calculator, text="Basic")

        # Map out what buttons to place and where
        self.buttons = {
            '1': (1, 0),
            '2': (1, 1),
            '3': (1, 2),
            '4': (2, 0),
            '5': (2, 1),
            '6': (2, 2),
            '7': (3, 0),
            '8': (3, 1),
            '9': (3, 2),
            '0': (4, 0),
            '+': (5, 0),
            '-': (5, 1),
            '*': (5, 2),
            '/': (5, 3),
            '=': (6, 1, 2),
            'C': (4, 1, 2)
        }
>>>>>>> parent of 0d58d06 (Modified structure for expandability)

        self.create_buttons()

        # Use running variables to store the current user entries
        self.current_operation = None
        self.first_number = None

    def create_buttons(self):
        # Loop over all buttons in the buttons object
        for key, value in self.buttons.items():
            # Determine how much space each button needs
            row, col = value[:2]
            colspan = value[2] if len(value) > 2 else 1
            # Assign a Tkinter dimension to the button
            button = tk.Button(self, text=key, padx=40, pady=20)
            button.grid(row=row, column=col, columnspan=colspan)
            # Configure button actions for each operation and click handling
            if key in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                button.configure(command=lambda x=key: self.number_click(x))
            elif key == '+':
                button.configure(command=self.add_click)
            elif key == '-':
                button.configure(command=self.sub_click)
            elif key == '*':
                button.configure(command=self.mul_click)
            elif key == '/':
                button.configure(command=self.div_click)
            elif key == '=':
                button.configure(command=self.equal_click)
            elif key == 'C':
                button.configure(command=self.clear_click)

    def number_click(self, number):
        # Get the current display value
        current = self.display.get()
        # Clear the entire display
        self.display.delete(0, tk.END)
        # Update the display with the old display value plus the recently pressed button
        self.display.insert(0, str(current) + str(number))

    def clear_click(self):
        # Clear out the display by deleting everything
        self.display.delete(0, tk.END)

    def add_click(self):
        # Obtain current number from display
        self.first_number = int(self.display.get())
        # Use an anonymous function to pass for addition
        self.current_operation = lambda x, y: x + y
        # Clear display for next number
        self.display.delete(0, tk.END)

    def sub_click(self):
        self.first_number = int(self.display.get())
        # Same as add_click, but with different anonymous functions
        self.current_operation = lambda x, y: x - y
        self.display.delete(0, tk.END)

    def mul_click(self):
        self.first_number = int(self.display.get())
        self.current_operation = lambda x, y: x * y
        self.display.delete(0, tk.END)

    def div_click(self):
        self.first_number = int(self.display.get())
        self.current_operation = lambda x, y: x / y
        self.display.delete(0, tk.END)

    def equal_click(self):
        # Obtain second number after first operation
        second_number = int(self.display.get())
        self.display.delete(0, tk.END)
        # Run the calculation using the function passed for current_operation
        result = self.current_operation(self.first_number, second_number)
        # Print the result
        self.display.insert(0, result)


if __name__ == '__main__':
    # Start Tkinter application
    app = Calculator()
    app.mainloop()
