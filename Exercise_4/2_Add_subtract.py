def sum_numbers(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def add_and_subtract(digit1, digit2, digit3):
    return subtract(sum_numbers(digit1, digit2), digit3)


first = int(input())
second = int(input())
third = int(input())
print(add_and_subtract(first,second,third))