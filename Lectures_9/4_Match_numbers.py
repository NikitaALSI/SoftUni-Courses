import re
numbers = input()
pat = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
matches = [match.group() for match in re.finditer(pat, numbers)]

print(" ".join(matches))