import re

key = list(map(int, input().split()))

while (string := input()) != "find":
    message = ""
    key_index = 0
    for char in string:
        message += chr(ord(char) - key[key_index])
        key_index += 1
        if key_index == len(key):
            key_index = 0

    pat = r"&(.+)&.+<(.+)>"
    item, coordinates = re.search(pat, message).groups()
    print(f"Found {item} at {coordinates}")
