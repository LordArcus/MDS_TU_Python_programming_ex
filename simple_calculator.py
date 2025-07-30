# Write a program using match-case statement to develop a simple calculator.

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    match choice:
        case '1':
            result = num1 + num2
            operation = "Addition"
        case '2':
            result = num1 - num2
            operation = "Subtraction"
        case '3':
            result = num1 * num2
            operation = "Multiplication"
        case '4':
            if num2 == 0:
                return "Error! Division by zero."
            result = num1 / num2
            operation = "Division"
        case _:
            return "Invalid input"

    return f"{operation} result: {result}"


calculator_result = calculator()
print(calculator_result)