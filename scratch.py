import re

text = input()

pattern = r'>((\s*\w+\s*)+)<'
matches = re.findall(pattern, text)

filtered = list(filter(lambda x: x != "\\n", matches))

texts = []
for part in filtered:
    text = part.replace("\\n", "")
    text = text.strip()
    texts.append(text)

print(f"Title: {texts[0]}\nContent: {' '.join(texts[1::])}")

