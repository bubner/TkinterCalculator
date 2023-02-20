# A Python GUI calculator built in Tkinter
# Lucas Bubner, 2023

import tkinter as tk
from tkinter import ttk
from design import create_standard
from operations import append, addc, subc, mulc, divc, equc, clrc


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
        self.basic_calculator = ttk.Frame(self.notebook)
        self.notebook.add(self.basic_calculator, text="Basic")

        # Add standard widgets to the default tab from design.py
        create_standard(self, self.basic_calculator)

    # Define class methods from operations.py
    append = append
    addc = addc
    subc = subc
    mulc = mulc
    divc = divc
    equc = equc
    clrc = clrc


if __name__ == "__main__":
    # Initialise new Tkinter application
    app = Calculator()
    app.mainloop()
