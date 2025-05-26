key = int(input())
char_count = int(input())
decrypted_text = ''
for i in range(char_count):
    char = input()
    new_char = chr(key + ord(char))
    decrypted_text += new_char

print(decrypted_text)