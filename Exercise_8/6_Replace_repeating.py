text = input()
unique = text[0]
for char in range(1, len(text)):
    if text[char] != unique[-1]:
        unique += text[char]
print(unique)