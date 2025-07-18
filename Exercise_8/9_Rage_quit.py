string = input()
new_string = ""
sub_string = ""
repeat = ""
for char in range(len(string)):
    if string[char].isdigit():
        repeat += string[char]
        if char != len(string)-1:
            continue

    if repeat:
        new_string += sub_string.upper()*int(repeat)
        repeat = ""
        sub_string = ""

    sub_string += string[char]

print(f"Unique symbols used: {len(set([x for x in new_string]))}\n{new_string}")
