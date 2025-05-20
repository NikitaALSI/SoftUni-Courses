coffee_needed = 0
while True:
    command = input()
    if command == "END":
        break

    if (command.lower() == "coding"
        or command.lower() == "dog"
        or command.lower() == "cat"
        or command.lower() == "movie"):
        if command.islower():
            coffee_needed += 1
        elif command.isupper():
            coffee_needed += 2
    else:
        continue

if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)