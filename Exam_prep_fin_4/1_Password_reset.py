password = input()

while (cmd := input()) != "Done":
    if cmd.startswith("TakeOdd"):
        password = "".join([password[index] for index in range(len(password)) if index % 2 != 0])
        print(password)
    elif cmd.startswith("Cut"):
        index, length = cmd.split()[1:]
        sub_string = password[int(index):min(len(password), int(index) + int(length))]
        password = password.replace(sub_string, "", 1)
        print(password)
    elif cmd.startswith("Substitute"):
        substring, substitute = cmd.split()[1:]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
print(f"Your password is: {password}")


