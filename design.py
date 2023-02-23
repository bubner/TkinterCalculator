# Tkinter app design module
import tkinter as tk
from operations import Operations
from PIL import ImageTk, Image


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
        '=': (7, 4, 2),
        'C': (2, 4, 2),
        '.': (2, 0),
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
        span = value[2] if len(value) > 2 else 1
        # Construct a button for each pair
        btn = tk.Button(target, text=key, width=5, height=2)
        btn.grid(row=row, column=col, columnspan=span, padx=5, pady=5)
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
        'sin': (4, 5),
        'cos': (5, 5),
        'tan': (6, 5),
        'log': (4, 4),
        'rand': (5, 4),
        '\u00B3√': (7, 1),
        'x\u00B2': (7, 2),
        'x\u00B3': (7, 3),
        'x!': (6, 4),
        '\u221A': (7, 0),
        '(': (3, 4),
        ')': (3, 5),
    }

    # Add the scientific buttons by looping over each button and it's coordinates
    for key, value in buttons.items():
        # Unpack the values from the buttons object by slicing the tuple in the value pair
        row, col = value[:2]
        span = value[2] if len(value) > 2 else 5
        # Construct a button for each pair
        btn = tk.Button(target, text=key, width=span, height=2)
        btn.grid(row=row, column=col, columnspan=1, padx=5, pady=5)
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
        elif key == 'rand':
            btn.configure(command=lambda: self.changeop(Operations.RANDOM))


def create_graphing(self, target):
    # Create graph area
    self.graph = tk.Canvas(target, width=300, height=300)
    self.graph.grid(row=0, column=0, columnspan=100, pady=5)

    # Create input box label
    self.graph_input_label = tk.Label(target, text="y = ")
    self.graph_input_label.grid(row=1, column=0, columnspan=10, pady=5)

    # Create input box
    self.graph_input = tk.Entry(target, width=25)
    self.graph_input.grid(row=1, column=1, columnspan=100, pady=5)

    # Create graph button
    self.graph_button = tk.Button(target, text="Plot", width=5, height=2)
    self.graph_button.grid(row=2, column=0, columnspan=100, pady=5)
    self.graph_button.configure(command=self.graphc)

    # Create reset graph button that is right to the graph button
    self.reset_button = tk.Button(target, text="Reset", width=5, height=2)
    self.reset_button.grid(row=2, column=1, columnspan=40, pady=5)
    self.reset_button.configure(command=self.resetc)

    # Create x and y line placeholders by calling reset function
    self.resetc()


def create_trig(self, target):
    # TODO: Triangle image
    # img = ImageTk.PhotoImage(Image.open(r"assets/triangle-right.png"))
    # self.image = tk.Label(target, image=img)
    # self.image.place(x=100, y=200)
    
    # Side a
    self.a = tk.Entry(target, width=30)
    self.a.grid(row=0, column=1, columnspan=1, pady=5)
    self.a_label = tk.Label(target, text="side a: ")
    self.a_label.grid(row=0, column=0, columnspan=1, pady=5)

    # Side b
    self.b = tk.Entry(target, width=30)
    self.b.grid(row=1, column=1, columnspan=10, pady=5)
    self.b_label = tk.Label(target, text="side b: ")
    self.b_label.grid(row=1, column=0, columnspan=1, pady=5)

    # Side c
    self.c = tk.Entry(target, width=30)
    self.c.grid(row=2, column=1, columnspan=10, pady=5)
    self.c_label = tk.Label(target, text="side c: ")
    self.c_label.grid(row=2, column=0, columnspan=1, pady=5)

    # Angle A
    self.A = tk.Entry(target, width=30)
    self.A.grid(row=3, column=1, columnspan=10, pady=5)
    self.A_label = tk.Label(target, text="angle A (deg): ")
    self.A_label.grid(row=3, column=0, columnspan=1, pady=5)
    
    # Angle B
    self.B = tk.Entry(target, width=30)
    self.B.grid(row=4, column=1, columnspan=10, pady=5)
    self.B_label = tk.Label(target, text="angle B (deg): ")
    self.B_label.grid(row=4, column=0, columnspan=1, pady=5)

    # Solve button
    self.solve_button = tk.Button(target, text="Solve", width=5, height=2)
    self.solve_button.grid(row=10, column=0, columnspan=1, pady=5)
    self.solve_button.configure(command=self.trigc)

    # TODO: Clear button

    # Complaint text
    self.complaint = tk.Label(target, text="")
    self.complaint.grid(row=10, column=1, columnspan=1)
    