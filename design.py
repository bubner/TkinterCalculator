# Tkinter app design module
import tkinter as tk
from operations import Operations


# Function to create the standard 0 to 9, clear, equal, and arithmatic operations design
def create_standard(self, target):
    # Dictionary of buttons to map with standard grid positions
    buttons = {
        '1': (5, 0),
        '2': (5, 1),
        '3': (5, 2),
        '4': (4, 0),
        '5': (4, 1),
        '6': (4, 2),
        '7': (3, 0),
        '8': (3, 1),
        '9': (3, 2),
        '0': (6, 1),
        '+': (3, 3),
        '-': (4, 3),
        '*': (5, 3),
        '/': (6, 3),
        '=': (6, 2),
        'C': (2, 0),
        '.': (6, 0),
        '-/+': (2, 1),
        '\u03C0': (2, 2),
        '\u2190': (2, 3),
    }

    # Add the entry widget to display the calculation
    self.display = tk.Entry(target, width=25)
    self.display.grid(row=1, column=0, columnspan=100, pady=5)

    # Add a small widget above the entry bar that displays the current calculation
    self.current = tk.Label(target, text="Calculator")
    self.current.grid(row=0, column=0, columnspan=100, pady=5)

    # Add the number buttons by looping over each button and it's coordinates
    for key, value in buttons.items():
        # Unpack the values from the buttons object by slicing the tuple in the value pair
        row, col = value[:2]
        colspan = value[2] if len(value) > 2 else 1
        # Construct a button for each pair
        btn = tk.Button(target, text=key, width=5, height=2)
        btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)
        # Change colour to grey
        btn.configure(bg="#d3d3d3")
        # Assign operations to each button
        if key in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            btn.configure(command=lambda x=key: self.append(x))
        elif key == '+':
            btn.configure(command=lambda: self.changeop(Operations.ADDITION))
        elif key == '-':
            btn.configure(command=lambda: self.changeop(Operations.SUBTRACTION))
        elif key == '*':
            btn.configure(command=lambda: self.changeop(Operations.MULTIPLICATION))
        elif key == '/':
            btn.configure(command=lambda: self.changeop(Operations.DIVISION))
        elif key == '=':
            btn.configure(command=self.equc)
        elif key == 'C':
            btn.configure(command=self.clrc)
        elif key == '.':
            btn.configure(command=self.dotc)
        elif key == '-/+':
            btn.configure(command=self.negc)
        elif key == '\u03C0':
            btn.configure(command=self.pic)
        elif key == '\u2190':
            btn.configure(command=self.delc)


# Append scientific functions to the calculator interface
def append_scientific(self, target):
    # Dictionary of all scientific calculation buttons
    buttons = {
        'sin': (2, 4),
        'cos': (3, 4),
        'tan': (4, 4),
        'log': (5, 4),
        'mod': (6, 4),
        'x\u00B2': (7, 2),
        'x\u00B3': (7, 3),
        'e\u02E3': (7, 4),
        'x!': (7, 0),
        '\u221A': (7, 1),
        'sin\u207B\u00B9': (2, 5),
        'cos\u207B\u00B9': (3, 5),
        'tan\u207B\u00B9': (4, 5),
        'ln': (5, 5),
        '(': (6, 5),
        ')': (7, 5),
    }

    # Add the scientific buttons by looping over each button and it's coordinates
    for key, value in buttons.items():
        # Unpack the values from the buttons object by slicing the tuple in the value pair
        row, col = value[:2]
        colspan = value[2] if len(value) > 2 else 1
        # Construct a button for each pair
        btn = tk.Button(target, text=key, width=5, height=2)
        btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)
        # Assign operations to each button
        if key == 'sin':
            btn.configure(command=lambda: self.changeop(Operations.SINE))
        elif key == 'cos':
            btn.configure(command=lambda: self.changeop(Operations.COSINE))
        elif key == 'tan':
            btn.configure(command=lambda: self.changeop(Operations.TANGENT))
        elif key == 'log':
            btn.configure(command=lambda: self.changeop(Operations.LOGARITHM))
        elif key == 'mod':
            btn.configure(command=lambda: self.changeop(Operations.MODULUS))
        elif key == 'x\u00B2':
            btn.configure(command=lambda: self.changeop(Operations.SQUARE))
        elif key == 'x\u00B3':
            btn.configure(command=lambda: self.changeop(Operations.CUBE))
        elif key == 'e\u02E3':
            btn.configure(command=lambda: self.changeop(Operations.EXPONENT))
        elif key == 'x!':
            btn.configure(command=lambda: self.changeop(Operations.FACTORIAL))
        elif key == '\u221A':
            btn.configure(command=lambda: self.changeop(Operations.SQUARE_ROOT))
        elif key == 'sin\u207B\u00B9':
            btn.configure(command=lambda: self.changeop(Operations.ASINE))
        elif key == 'cos\u207B\u00B9':
            btn.configure(command=lambda: self.changeop(Operations.ACOSINE))
        elif key == 'tan\u207B\u00B9':
            btn.configure(command=lambda: self.changeop(Operations.ATANGENT))
        elif key == 'ln':
            btn.configure(command=lambda: self.changeop(Operations.NATURAL_LOG))
        elif key == '(':
            btn.configure(command=lambda: self.brac("("))
        elif key == ')':
            btn.configure(command=lambda: self.brac(")"))
