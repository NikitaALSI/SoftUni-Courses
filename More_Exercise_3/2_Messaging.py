sequence = input().split(" ")
code = [char for char in input()]
message = ""

for number in sequence:
    index = sum([int(digit) for digit in number])
    message += code.pop(index - len(code) if index >= len(code) else index)

print(message)
