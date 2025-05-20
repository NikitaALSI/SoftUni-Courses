n = int(input())

for code in range(n):
    number = int(input())
    message = ""

    if number == 88:
        message = "Hello"
    elif number == 86:
        message = "How are you?"
    elif number < 88:
        message = "GREAT!"
    else:
        message = "Bye."

    print(message)