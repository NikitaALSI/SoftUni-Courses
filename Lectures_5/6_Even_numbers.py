number_list = input().split(", ")
even_numbers = [number if int(number) % 2 == 0 else "no" for number in number_list]
even_number_indices = []
for number in even_numbers:
    if number != "no":
        even_number_indices.append(even_numbers.index(number))
        even_numbers[even_numbers.index(number)] = "no"

print(even_number_indices)