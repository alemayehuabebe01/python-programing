#   python calculator program using python 3.83

#   calculator

#   addition function

def add(n1, n2):
    return n1 + n2


#   subtract function

def subtract(n1, n2):
    return n1 - n2


#   multiply function

def multiply(n1, n2):
    return n1 * n2


#   divide function

def divide(n1, n2):
    return n1 / n2


#   create a dictionary tha hold all the operator and function name

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the first number ? :"))
    for operator in operations:
        operands = operator
        print(operands)
    will_cont = False
    while not will_cont:

        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number ? :"))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} =  {result}")

        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit. :")

        if should_continue == 'y':
            num1 = result
        else:
            will_cont = True
            calculator()


calculator()
