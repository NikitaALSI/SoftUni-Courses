import re
dates = input()
pat = r'\b(\d{2})(\.|\-|\/)([A-Z][a-z]{2})\2([0-9]{4})\b'
matches = [match.groups() for match in re.finditer(pat, dates)]

for match in matches:
    day = match[0]
    month = match[2]
    year = match[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")