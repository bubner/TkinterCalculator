# Tkinter app design module
import tkinter as tk

# Function to create the standard 0 to 9, clear, equal, and arithmatic operations design
def create_standard(self, target):
    # Dictionary of buttons to map with standard grid positions
    buttons = {
        '1': (3, 0),
        '2': (3, 1),
        '3': (3, 2),
        '4': (2, 0),
        '5': (2, 1),
        '6': (2, 2),
        '7': (1, 0),
        '8': (1, 1),
        '9': (1, 2),
        '0': (4, 1),
        '+': (1, 3),
        '-': (2, 3),
        '*': (3, 3),
        '/': (4, 3),
        '=': (4, 2),
        'C': (4, 0)
    }

    # Add the entry widget to display the calculation
    self.display = tk.Entry(target, width=25)
    self.display.grid(row=0, column=0, columnspan=4, pady=5)

    # Add the number buttons by looping over each button and it's coordinates
    for key, value in buttons.items():
        # Unpack the values from the buttons object by slicing the tuple in the value pair
        row, col = value[:2]
        colspan = value[2] if len(value) > 2 else 1
        # Construct a button for each pair
        btn = tk.Button(self.basic_calculator, text=key, width=5, height=2)
        btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)
        # Assign operations to each button
        if key in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            btn.configure(command=lambda x=key: self.append(x))
        elif key == '+':
            btn.configure(command=self.addc())
        elif key == '-':
            btn.configure(command=self.subc())
        elif key == '*':
            btn.configure(command=self.mulc())
        elif key == '/':
            btn.configure(command=self.divc())
        elif key == '=':
            btn.configure(command=self.equc())
        elif key == 'C':
            btn.configure(command=self.clrc())
