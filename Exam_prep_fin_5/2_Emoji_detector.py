import re

text = input()

emoji_pat = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"
coolness_pat = r"[A-Za-z]"
threshold_pat = r"\d"

threshold_list = list(map(int, re.findall(threshold_pat, text)))
threshold = 1
for digit in threshold_list:
    threshold *= digit
print(f"Cool threshold: {threshold}")

emojis = [x.group() for x in re.finditer(emoji_pat, text)]
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in emojis:
    coolness = sum(list(map(lambda x: ord(x), re.findall(coolness_pat, emoji))))
    if coolness >= threshold:
        print(emoji)

