import re


text = input()
pat = r'([@#])([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)'
pairs = re.finditer(pat, text)
pairs_list = [x for x in pairs]
matches = [f"{x.group(2)} <=> {x.group(5)}" for x in list(filter(lambda x: x.group(2) == x.group(5)[::-1], pairs_list))]
if pairs_list:
    print(f"{len(pairs_list)} word pairs found!")
else:
    print(f"No word pairs found!")

if matches:
    print(f"The mirror words are:\n{', '.join(matches)}")
else:
    print(f"No mirror words!")