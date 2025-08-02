import re

pat = r'\d+'

while (line := input()) != '':
    numbers = re.findall(pat, line)
    for number in numbers:
        print(number, end=" ")
