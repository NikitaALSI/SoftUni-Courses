import re
sentence = input()
word = input()
pat = rf'\b{word}\b'
occurrences = re.findall(pat, sentence, re.I)
print(len(occurrences))
