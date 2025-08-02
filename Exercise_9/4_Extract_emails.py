import re

# pat = r'\s(([a-z0-9]+[a-z0-9\-\.\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'
pat = r'\s([a-z0-9][a-z0-9\-\._]+[a-z0-9]@([a-z][a-z\-]+[a-z])+(\.[a-z]+)+)\b'
string = input()
emails = re.finditer(pat, string, re.I)
for email in emails:
    print(email.group(1))
