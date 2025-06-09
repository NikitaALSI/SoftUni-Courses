def chars_from_ascii(start: str, stop: str) -> str:
    string = ""
    for i in range(ord(start)+1, ord(stop)):
        string += chr(i)
        if i != ord(stop) - 1:
            string += " "
    return string


first = input()
second = input()
print(chars_from_ascii(first, second))

