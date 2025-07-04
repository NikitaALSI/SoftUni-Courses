words = input().split()
occurrences = {}
for word in words:
    occurrences[word.lower()] = occurrences.get(word.lower(), 0) + 1

for word in occurrences:
    if occurrences[word] % 2 != 0:
        print(word, end=" ")
