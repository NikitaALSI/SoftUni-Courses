MORSE_TO_ENG_DICT = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                     '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                     '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                     '-.--': 'Y', '--..': 'Z'}

message = input().split("|")
translated = ""
for word in message:
    letters = word.split()
    for letter in letters:
        translated += MORSE_TO_ENG_DICT[letter]
    translated += " "

print(translated)
