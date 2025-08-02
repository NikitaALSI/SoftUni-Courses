import re

pat = r'\b_([a-zA-Z0-9]+)\b'
sentence = input()
names = re.finditer(pat, sentence)
name_list =[]
for name in names:
    name_list.append(name.group(1))

print(",".join(name_list))