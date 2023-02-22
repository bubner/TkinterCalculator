# Operation and button handler module
import math
import tkinter as tk

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
    SINE = 5
    COSINE = 6
    TANGENT = 7
    LOGARITHM = 8
    MODULUS = 9
    SQUARE = 10
    CUBE = 11
    EXPONENT = 12
    FACTORIAL = 13
    SQUARE_ROOT = 14
    ASINE = 15
    ACOSINE = 16
    ATANGENT = 17
    NATURAL_LOG = 18

    operations_dict = {
        # Standard arithmetic operations
        ADDITION: lambda x, y: x + y,
        SUBTRACTION: lambda x, y: x - y,
        MULTIPLICATION: lambda x, y: x * y,
        DIVISION: lambda x, y: x / y,
        # Scientific operations
        SINE: lambda x: math.sin(math.radians(x)),
        COSINE: lambda x: math.cos(math.radians(x)),
        TANGENT: lambda x: math.tan(math.radians(x)),
        LOGARITHM: lambda x: math.log10(x),
        MODULUS: lambda x, y: x % y,
        SQUARE: lambda x: x ** 2,
        CUBE: lambda x: x ** 3,
        EXPONENT: lambda x: math.exp(x),
        FACTORIAL: lambda x: math.factorial(x),
        SQUARE_ROOT: lambda x: math.sqrt(x),
        ASINE: lambda x: math.asin(x),
        ACOSINE: lambda x: math.acos(x),
        ATANGENT: lambda x: math.atan(x),
        NATURAL_LOG: lambda x: math.log(x)
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
        elif operand == 5:
            string += "(sin)"
        elif operand == 6:
            string += "(cos)"
        elif operand == 7:
            string += "(tan)"
        elif operand == 8:
            string += "(log)"
        elif operand == 9:
            string += "(mod)"
        elif operand == 10:
            string += "(sqr)"
        elif operand == 11:
            string += "(cube)"
        elif operand == 12:
            string += "(exp)"
        elif operand == 13:
            string += "(fact)"
        elif operand == 14:
            string += "(sqrt)"
        elif operand == 15:
            string += "(asin)"
        elif operand == 16:
            string += "(acos)"
        elif operand == 17:
            string += "(atan)"
        elif operand == 18:
            string += "(ln)"
        elif operand == str(math.pi):
            string += "\u03C0"
        else:
            string += str(operand) if operand else ""
    return string


# Save the current numbers that are on the display
def save(self):
    if self.display.get() == "":
        # Check if the user is changing their operation from an arithmetic one
        if len(operands) > 0:
            # If so, replace the last operation with the new one
            if operands[-1] in (1, 2, 3, 4):
                operands[-1] = operation
            else:
                # If the user is pressing an operation after a scientific modifier
                # then we can simply append their new operation to the end
                operands.append(operation)
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


# Change the operation
def changeop(self, op: Operations):
    global operation
    # Set the operation to the new operation
    operation = op
    # Save the current numbers on the display including the operation type
    save(self)


# Finalise the operands array and equate an answer
def equc(self):
    global operands
    if len(operands) == 0:
        return

    i = 0
    operation_found = False
    # Run a loop over the operands array using a manual index loop
    while i < len(operands):
        # Check if the operand is a scientific function
        if isinstance(operands[i], int):
            if 5 <= operands[i] <= 18:
                # Use the dictionary to get the correct operation function
                operands[i] = str(Operations.operations_dict[operands[i]](float(operands[i - 1])))
                # Delete previous operand, as we've used it now
                del operands[i - 1]
                # Decrement the index to account for the deleted element
                i -= 1
            operation_found = True
        i += 1

    if not operation_found:
        # Don't run the calculation cycle if there's nothing we can calculate
        return

    # Reset operation target
    global operation
    operation = None

    # Append final numbers to the top bar only if there are any
    save(self) if self.display.get() != "" else None

    # Check if the end of the operands array ends with an operation denoted by an int
    if isinstance(operands[-1], int):
        operands.pop()
        # Update the top bar
        self.display.delete(0, tk.END)
        self.current.configure(text=get_operands())

    # Solve the equation listed by all the elements in the operands array
    result = operands[0] if operands[0] not in ("(", ")") else operands[1]

    # Use Order of Operations to solve the operands equation
    # The operands array is a structure of both integers and strings to indicate
    #   a) an operation
    #   b) a number
    #   c) a scientific function
    # Example, operands array would look like this for the equation (2 + 2) * 2
    # >>> ['(', '2', 1, '2', ')', 3, '2']
    # This algorithm has a time complexity of O(n) where n is the number of elements in the operands array
    # as it has to loop over the array twice in finding operations and then solving them
    # The bracket finding algorithm has a time complexity of O(n^2), as it needs to search for the
    # other bracket pair in the array. This is not ideal, but for the scope of this project is acceptable
    try:
        def solve(equation):
            res = result
            for i in range(1, len(equation), 2):
                # Check if the operation is multiplication or division
                if equation[i] == Operations.MULTIPLICATION or equation[i] == Operations.DIVISION:
                    # Use the dictionary to get the correct operation function
                    res = Operations.operations_dict[equation[i]](float(res), float(equation[i + 1]))
                    # Set the equation to 0, so they are not used again
                    equation[i] = equation[i + 1] = 0

            for i in range(1, len(equation), 2):
                # Check if the operation is addition or subtraction, and repeat solving process
                if equation[i] == Operations.ADDITION or equation[i] == Operations.SUBTRACTION:
                    res = Operations.operations_dict[equation[i]](float(res), float(equation[i + 1]))
                    equation[i] = equation[i + 1] = 0
            return res

        # Look for brackets and solve whatever is inside them first
        j = 0
        while j < len(operands):
            # Check if the operand is a bracket
            if operands[j] == "(":
                # Find the matching bracket
                for k in range(i, len(operands)):
                    # Check if the operand is a bracket or reached the end
                    if operands[k] == ")" or k == len(operands) - 1:
                        # Solve the equation inside the brackets
                        result = solve(operands[j + 1:k])
                        # Replace the occupied space between the brackets with the result
                        operands[j:k - 1] = [result]
                        # Adjust counter to account for the new length of the operands array
                        j = k - 1
                        break
            j += 1
        # Solve the rest of the equation
        result = solve(operands)
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
    # Must explicitly check for None as 0 is a valid result
    if result is not None:
        # Attempt to get rid of the .0 at the end of the result if applicable
        try:
            # Avoids rounding the number by checking if the int version of the result is the same as the float version
            result = int(result) if result == int(result) else result
        except ValueError:
            # Ignore any errors as it means the number is not a whole number
            pass
        # Update the display with the result
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
    if not operation:
        operation = Operations.MULTIPLICATION
    save(self)

    # Clear the entire display
    self.display.delete(0, tk.END)
    # Update the display with the old display value plus pi
    self.display.insert(0, str(math.pi))
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


# Handle placing brackets
def brac(self, bracket: str):
    # Don't allow the user to place a closing bracket if there is no opening bracket
    if bracket == ")" and operands.count("(") == 0:
        return
    # Don't allow the user to place an opening or closing bracket if one already exists
    # This is done as multiple brackets in the same operands array will cause issues
    if (bracket == "(" and operands.count("(") > 0) or (bracket == ")" and operands.count(")") > 0):
        return
    # Save current display value
    save(self)
    # Check if the final operand is an operation and remove it
    if len(operands) > 0 and isinstance(operands[-1], int):
        operands.pop()
    # Clear the entire display
    self.display.delete(0, tk.END)
    # Update the display with the old display value plus the bracket
    self.display.insert(0, bracket)
    save(self)


# Clear everything and reset the calculator
def clrc(self):
    global operation
    global operands
    operation = None
    operands.clear()
    self.display.delete(0, tk.END)
    self.current.configure(text="Calculator")
