message = input()

while (cmd := input()) != "Reveal":
    if cmd.startswith("InsertSpace"):
        index = int(cmd.split(":|:")[-1])
        message = message[:index] + " " + message[index:]
    elif cmd.startswith("Reverse"):
        substring = cmd.split(":|:")[-1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message = message + substring[::-1]
        else:
            print("error")
            continue
    elif cmd.startswith("ChangeAll"):
        substring, replacement = cmd.split(":|:")[1:]
        message = message.replace(substring, replacement)
    print(message)
print(f"You have a new text message: {message}")