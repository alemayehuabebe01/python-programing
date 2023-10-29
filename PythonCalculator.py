#  calculator in python

#  here if you can get an internet  you have to add the logo here

# Addition

def add(n1, n2):
    return n1 + n2


#  Subtract

def subtract(n1, n2):
    return n1 - n2


#  multiply

def multiply(n1, n2):
    return n1 * n2


#  divide

def divide(n1, n2):
    return n1 / n2


#  create dictionary

operations = {
    "+": add,
    "*": multiply,
    "-": subtract,
    "/": divide,
}


#   recursion function the function that call itself used to refresh the given system

def calculator():
    condition = True
    while condition:
        num1 = float(input("What's the First number ?:"))

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What is the second number?:"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
            num1 = answer
        else:
            condition = False
            calculator()


calculator()
