# A Python GUI calculator built in Tkinter
# Lucas Bubner, 2023

import tkinter as tk
from tkinter import ttk
from design import create_standard, append_scientific, create_graphing, create_trig
import operations as op


class Calculator(tk.Tk):
    def __init__(self):
        # Initialise a new Tkinter class
        super().__init__()

        # Assign window title
        self.title("Calculator")

        # Change favicon if we can
        try:
            self.iconbitmap(r"./assets/favicon.ico")
        except tk.TclError:
            # If the favicon is not supported, it will throw an error. However, we can safely swallow it.
            pass

        # Prevent resizing
        self.resizable(False, False)

        # Create a Notebook widget for multiple tabs
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create the default tab
        self.scientific_calculator = ttk.Frame(self.notebook)
        self.notebook.add(self.scientific_calculator, text="Calculator")

        # Create a graphing tab
        self.graphing_calculator = ttk.Frame(self.notebook)
        self.notebook.add(self.graphing_calculator, text="Graphing")

        # Create a trig tab
        self.trig_calculator = ttk.Frame(self.notebook)
        self.notebook.add(self.trig_calculator, text="Right Angle Trigonometry")

        # Add standard widgets to the basic calculator tab
        create_standard(self, self.scientific_calculator)

        # Append the scientific functions to the calculator interface
        append_scientific(self, self.scientific_calculator)

        # Add the graphing calculator to the graphing tab
        create_graphing(self, self.graphing_calculator)

        # Add the trigonometry calculator to the trig tab
        create_trig(self, self.trig_calculator)

    # Define class methods from operations.py
    append = op.append
    changeop = op.changeop
    equc = op.equc
    clrc = op.clrc
    dotc = op.dotc
    negc = op.negc
    pic = op.pic
    delc = op.delc
    brac = op.brac
    graphc = op.graphc
    resetc = op.resetc
    trigc = op.trigc


if __name__ == "__main__":
    # Initialise new Tkinter application
    app = Calculator()
    app.mainloop()
