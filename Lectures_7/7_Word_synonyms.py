n = int(input())
dictionary = {}

for _ in range(n):
    word = input()
    synonym = input()
    dictionary[word] = dictionary.get(word, []) + [synonym]

for word in dictionary:
    print(f"{word} - {', '.join(dictionary[word])}")
