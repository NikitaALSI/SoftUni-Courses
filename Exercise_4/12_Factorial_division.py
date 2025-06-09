def factorial_of_whole_number(num1: int) -> float:
    factorial = 1
    for i in range(1, num1+1):
        factorial *= i
    return factorial


first = factorial_of_whole_number(int(input()))
second = factorial_of_whole_number(int(input()))
print(f"{first/second:.2f}")
