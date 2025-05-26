number_of_chars = int(input())
char_ascii_value = 0
for repeats in range(number_of_chars):
    char = input()
    char_ascii_value += ord(char)

print(f"The sum equals: {char_ascii_value}")
