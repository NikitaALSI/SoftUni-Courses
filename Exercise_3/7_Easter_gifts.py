gifts = input().split()

while True:
    command = input().split()
    if command == "No Money".split():
        break
    elif "OutOfStock" in command:
        while command[1] in gifts:
            gifts[gifts.index(command[1])] = "None"
    elif "Required" in command:
        if int(command[2]) in range(len(gifts)):
            gifts[int(command[2])] = command[1]
    elif "JustInCase" in command:
        gifts[-1] = command[-1]

while "None" in gifts:
    gifts.remove("None")

print(" ".join(gifts))
