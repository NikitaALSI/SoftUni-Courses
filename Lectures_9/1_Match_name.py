import re
names = input()
pat = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
matches = re.findall(pat, names)
print(" ".join(matches))
