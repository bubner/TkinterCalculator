# Operation and button handler module
import tkinter as tk
import math

# Use global variables for storing the operation and operands
operation = None
operands = []


# Define an enum with the actual operation functions and a dictionary to map them
class Operations:
    # Allows for a static enum in Python (for example, Operations.ADDITION)
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4

    operations_dict = {
        # Using anonymous functions to define the operations
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


# Get the operands array as a string, checking if it is an int matching 1-4 then assigning them values accordingly
def get_operands():
    global operands
    string = ""
    for operand in operands:
        # Check if the operand matches an INTEGER of the ints 1,4 as we will know they are operations not user input
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
        # Check if the user is changing their operation instead
        if len(operands) > 0:
            # If so, replace the last operation with the new one
            operands[-1] = operation
            # Update the current calculation label
            self.current.configure(text=get_operands())
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
    if len(operands) == 0:
        return
    global operation

    # Append final numbers to the top bar
    operation = None
    save(self)

    # Check if the end of the operands array ends with an operation denoted by an int
    if isinstance(operands[-1], int):
        operands.pop()
        # Update the top bar
        self.display.delete(0, tk.END)
        self.current.configure(text=get_operands())

    # Solve the equation listed by all the elements in the operands array
    result = operands[0]

    # Use order of operations to solve multiplication and division first
    try:
        for i in range(1, len(operands), 2):
            # Check if the operation is multiplication or division
            if operands[i] == 3 or operands[i] == 4:
                # Use the dictionary to get the correct operation function
                result = Operations.operations_dict[operands[i]](float(result), float(operands[i + 1]))
                # Set the operands to 0, so they are not used again
                operands[i] = 0
                operands[i + 1] = 0

        for i in range(1, len(operands), 2):
            # Check if the operation is addition or subtraction
            if operands[i] == 1 or operands[i] == 2:
                # Perform the same operation as above
                result = Operations.operations_dict[operands[i]](float(result), float(operands[i + 1]))
                operands[i] = 0
                operands[i + 1] = 0
    except ValueError:
        # If the user inputs an illegal character, display an error message
        self.current.configure(text="Input was illegal.")
        result = None
    except ZeroDivisionError:
        # If the user tries to divide by zero, display an error message
        self.current.configure(text="Division by zero is illegal.")
        result = None
    finally:
        # Always clear the operands array and display
        operands.clear()
        self.display.delete(0, tk.END)

    # Insert the result into the display if nothing went wrong and result is not null
    if result:
        # Attempt to get rid of the .0 at the end of the result if applicable
        # We can do this by checking if the result is divisible by 1 evenly
        if result % 1 == 0:
            result = int(result)
        self.display.insert(0, result)


# Handle clicking the period key
def dotc(self):
    # Get the current display value
    current = self.display.get()
    # Check if the current display value contains a period
    if "." in current:
        return
    # Clear the entire display
    self.display.delete(0, tk.END)
    # Update the display with the old display value plus the recently pressed button
    self.display.insert(0, str(current) + ".")


# Handle inserting pi
def pic(self):
    global operation
    # Get the current display value
    current = self.display.get()
    operation = Operations.MULTIPLICATION
    save(self)

    # Clear the entire display
    self.display.delete(0, tk.END)
    # Update the display with the old display value plus pi
    self.display.insert(0, str(current) + str(math.pi))
    save(self)


# Handle changing the current number into negative
def negc(self):
    # Get the current display value
    current = self.display.get()
    if current == "":
        return
    # Check if the current display value is negative
    if current[0] == "-":
        # If it is, remove the negative sign
        current = current[1:]
    else:
        # If it is not, add the negative sign
        current = "-" + current
    # Clear the entire display
    self.display.delete(0, tk.END)
    # Update the display with the old display value plus the recently pressed button
    self.display.insert(0, str(current))


# Handle deleting the last character of the current display
def delc(self):
    # Get the current display value
    current = self.display.get()
    # Check if the current display value is empty
    if current == "":
        return
    # Clear the entire display
    self.display.delete(0, tk.END)
    # Update the display with the old display value minus the last character
    self.display.insert(0, current[:-1])


# Clear everything and reset the calculator
def clrc(self):
    global operation
    global operands
    operation = None
    operands.clear()
    self.display.delete(0, tk.END)
    self.current.configure(text="Calculator")
