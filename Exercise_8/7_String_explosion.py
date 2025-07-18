string = input()
skip = 0
new_string = ""
for char in range(len(string)):
    if string[char] == ">":
        skip += int(string[char+1])
        new_string += ">"
        continue

    if skip:
        skip -= 1
        continue
    else:
        new_string += string[char]
print(new_string)