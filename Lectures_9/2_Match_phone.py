import re
phones = input()
pat = r'\+359( |-)2(\1)[0-9]{3}(\1)[0-9]{4}\b'
matches = [match.group() for match in re.finditer(pat, phones)]
print(", ".join(matches))

