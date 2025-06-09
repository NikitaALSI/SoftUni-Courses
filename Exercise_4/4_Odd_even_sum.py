def odd_even_sum(list_of_numbers: str) ->str:
    odd_digits = [int(digit) for digit in list_of_numbers if int(digit) % 2 != 0]
    even_digits = [int(digit) for digit in list_of_numbers if int(digit) % 2 == 0]
    return f"Odd sum = {sum(odd_digits)}, Even sum = {sum(even_digits)}"


digits = input()
print(odd_even_sum(digits))