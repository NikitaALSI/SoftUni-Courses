message = input()

while (cmd := input()) != "Decode":
    if cmd.startswith("Move"):
        number_of_letters = int(cmd.split("|")[-1])
        message = message[number_of_letters:] + message[:number_of_letters]
    elif cmd.startswith("Insert"):
        index, value = cmd.split("|")[1:]
        message = message[:int(index)] + value + message[int(index):]
    elif cmd.startswith("Change"):
        substring, replacement = cmd.split("|")[1:]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")