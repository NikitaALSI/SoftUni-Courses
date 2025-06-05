def calculate(operator: str, num1: int, num2: int):
    calculations = {
        "multiply": num1 * num2,
        "divide": int(num1 / num2),
        "add": num1 + num2,
        "subtract": num1 - num2
    }
    return calculations[operator]


operator = input()
num1 = int(input())
num2 = int(input())

print(calculate(operator, num1, num2))