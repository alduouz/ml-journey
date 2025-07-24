# Simple Calculator

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter valid numbers!")

def get_operator():
    valid_operators = {'+', '-', '*', '/'}
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in valid_operators:
            return operator
        print("Error: Invalid operator! Please use +, -, *, or /")

def calculate(num1, num2, operator):
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else None
    }
    return operations[operator]

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")
operator = get_operator()

if operator == '/' and num2 == 0:
    print("Error: Division by zero!")
    num2 = get_number("Enter a non-zero second number: ")

result = calculate(num1, num2, operator)
print(f"Result: {num1} {operator} {num2} = {result}")