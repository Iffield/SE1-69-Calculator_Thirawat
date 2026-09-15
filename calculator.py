def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


expression = input("Enter calculation (example: 10 + 5): ")

num1, operator, num2 = expression.split()

num1 = float(num1)
num2 = float(num2)

if operator == "+":
    result = add(num1, num2)

