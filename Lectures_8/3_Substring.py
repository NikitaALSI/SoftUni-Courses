key = input()
word = input()
while key in word:
    word = word.replace(key, "")
print(word)