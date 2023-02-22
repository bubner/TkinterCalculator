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
        'rand': (6, 4),
        '\u00B3√': (7, 2),
        'x\u00B2': (7, 3),
        'x\u00B3': (7, 4),
        'x!': (7, 0),
        '\u221A': (7, 1),
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
        elif key == '\u00B3√':
            btn.configure(command=lambda: self.changeop(Operations.CUBE_ROOT))
        elif key == 'x\u00B2':
            btn.configure(command=lambda: self.changeop(Operations.SQUARE))
        elif key == 'x\u00B3':
            btn.configure(command=lambda: self.changeop(Operations.CUBE))
        elif key == 'x!':
            btn.configure(command=lambda: self.changeop(Operations.FACTORIAL))
        elif key == '\u221A':
            btn.configure(command=lambda: self.changeop(Operations.SQUARE_ROOT))
        elif key == '(':
            btn.configure(command=lambda: self.brac("("))
        elif key == ')':
            btn.configure(command=lambda: self.brac(")"))
        elif key == 'ln':
            btn.configure(command=lambda: self.changeop(Operations.NATURAL_LOG))
        elif key == 'rand':
            btn.configure(command=lambda: self.changeop(Operations.RANDOM))


def create_graphing(self, target):
    # Create graph area
    self.graph = tk.Canvas(target, width=300, height=300)
    self.graph.grid(row=0, column=0, columnspan=100, pady=5)

    # Create input box label
    self.graph_input_label = tk.Label(target, text="y = ")
    self.graph_input_label.grid(row=1, column=0, columnspan=40, pady=5)

    # Create input box
    self.graph_input = tk.Entry(target, width=25)
    self.graph_input.grid(row=1, column=1, columnspan=100, pady=5)

    # Create graph button
    self.graph_button = tk.Button(target, text="Plot", width=5, height=2)
    self.graph_button.grid(row=2, column=0, columnspan=100, pady=5)
    self.graph_button.configure(command=self.graphc)

    # Create x and y line placeholders
    self.graph.create_line(0, 150, 300, 150, width=2, fill='gray')
    self.graph.create_line(150, 0, 150, 300, width=2, fill='gray')
    self.graph.create_text(150, 150, text="No plot yet", font=("Arial", 16))
