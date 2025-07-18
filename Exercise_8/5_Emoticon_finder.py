text = input()
emoticons = []
for char in range(len(text)):
    if text[char] == ":":
        emoticons.append(text[char:char+2])
print("\n".join(emoticons))