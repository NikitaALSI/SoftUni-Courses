number = int(input())

for num in range(1, number + 1):
    special = False
    value_of_digits = 0
    for digit in str(num):
        value_of_digits += int(digit)
    if (value_of_digits == 5 or
            value_of_digits == 7 or
            value_of_digits == 11):
        special = True
    print(f"{num} -> {special}")