number = input()

digits = [digit for digit in number]
sorted_list = reversed(sorted(digits))
largest = ''
for digit in sorted_list:
    largest += digit

print(largest)

