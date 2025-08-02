username = input()

while (cmd := input()) != "Registration":
    if cmd.startswith("Letters"):
        case = cmd.split()[-1]
        if case == "Upper":
            username = username.upper()
        elif case == "Lower":
            username = username.lower()
        print(username)
    elif cmd.startswith("Reverse"):
        start, stop = list(map(int, cmd.split()[1:]))
        if start in range(len(username)) and stop in range(len(username)):
            part = username[start:stop + 1][::-1]
            print(part)
        else:
            continue
    elif cmd.startswith("Substring"):
        part = cmd.split()[-1]
        if part in username:
            username = username.replace(part, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {part}.")
    elif cmd.startswith("Replace"):
        char = cmd.split()[-1]
        username = username.replace(char, "-")
        print(username)
    elif cmd.startswith("IsValid"):
        char = cmd.split()[-1]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")

