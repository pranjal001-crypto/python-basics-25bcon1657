def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        return "Cannot divide by zero"
    else:
        return "Invalid operation"


x = 10
y = 5
operator = "+"

answer = calculate(x, y, operator)

print(f"{x} {operator} {y} = {answer}")
