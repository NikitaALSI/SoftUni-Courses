secret_message = input().split()
first_letters = []
the_rest = []
for word in secret_message:
    numbers = ''
    letters = []
    for char in word:
        if char.isdigit():
            numbers += char
        else:
            letters.append(char)

    letters[0], letters[-1] = letters[-1], letters[0]
    first_letters.append(chr(int(numbers)))
    the_rest.append("".join(letters))

final_message = " ".join(list(map(lambda x, y: x + y, first_letters, the_rest)))
print(final_message)