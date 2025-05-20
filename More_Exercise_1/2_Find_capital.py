word = input()
capital_index = []
for index, char in enumerate(word):
    if char.isupper():
        capital_index.append(index)

print(capital_index)