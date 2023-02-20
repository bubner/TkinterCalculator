# Operation and button handler module
import tkinter as tk

operation = None
operands = []


class Operations:
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4

    operations_dict = {
        ADDITION: lambda x, y: x + y,
        SUBTRACTION: lambda x, y: x - y,
        MULTIPLICATION: lambda x, y: x * y,
        DIVISION: lambda x, y: x / y,
    }


# Number appendage to the main display
def append(self, num):
    # Get the current display value
    current = self.display.get()
    # Clear the entire display
    self.display.delete(0, tk.END)
    # Update the display with the old display value plus the recently pressed button
    self.display.insert(0, str(current) + str(num))


# Get the operands array as a string, checking if it is an int startwith 1-4 then assigning them +, -, *, / accordingly
def get_operands():
    global operands
    string = ""
    for operand in operands:
        # Check if the operand matches an INTEGER of the nums 1,4 as we will know they are operations not user input
        if operand == 1:
            string += " + "
        elif operand == 2:
            string += " - "
        elif operand == 3:
            string += " * "
        elif operand == 4:
            string += " / "
        else:
            string += str(operand)
    return string

    
# Save the current numbers that are on the display
def save(self):
    if self.display.get() == "":
        return
    # Add the current display value to the operands array
    operands.append(self.display.get())
    # If there is also an operation, also add it to the operands array
    if operation:
        operands.append(operation)
    # Clear the entire display
    self.display.delete(0, tk.END)
    # Display operands in the current calculation label
    self.current.configure(text=get_operands())

    
# List that we are going to add the previous numbers to the calculation
def addc(self):
    global operation
    operation = Operations.ADDITION
    save(self)

    
# List that we are going to subtract the previous numbers to the calculation
def subc(self):
    global operation
    operation = Operations.SUBTRACTION
    save(self)

    
# List that we are going to multiply the previous numbers to the calculation
def mulc(self):
    global operation
    operation = Operations.MULTIPLICATION
    save(self)

    
# List that we are going to divide the previous numbers to the calculation
def divc(self):
    global operation
    operation = Operations.DIVISION
    save(self)

    
# Finalise the operands array and equate an answer
def equc(self):
    global operation
    # Append final numbers to the top bar
    operation = None
    save(self)

    
# Clear everything
def clrc(self):
    global operation
    global operands
    operation = None
    operands = []
    self.display.delete(0, tk.END)
    self.current.configure(text="Calculator")
