import re

text = input()

pattern = r'(?<=>)([a-zA-Z0-9- \\.]+)(?=<)'
matches = re.findall(pattern, text)
print(matches)
filtered = list(filter(lambda x: x != "\\n", matches))
print(filtered)
texts = []
for part in filtered:
    text = part.replace("\\n", "")
    texts.append(text)
print(texts)

print(f"Title: {filtered[0]} Content: {' '.join(texts[1::])}")

