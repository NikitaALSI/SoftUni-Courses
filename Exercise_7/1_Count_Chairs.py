text = input()
chars_count = {}

for char in text:
    if char != " ":
        chars_count[char] = chars_count.get(char, 0) + 1

for char, count in chars_count.items():
    print(f"{char} -> {count}")