text = [x for x in input()]
encrypted_text = "".join(list(map(lambda x: chr(ord(x)+ 3), text)))
print(encrypted_text)