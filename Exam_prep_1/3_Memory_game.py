elements = input().split()
number_of_moves = 0
while True:
    command = input()
    if command == "end":
        print(f"Sorry you lose :(\n"
              f"{' '.join(elements)}")
        break

    index1, index2 = list(map(int, command.split()))
    number_of_moves += 1
    if index1 == index2 or index1 not in range(len(elements)) or index2 not in range(len(elements)):
        print("Invalid input! Adding additional elements to the board")
        elements.insert(len(elements)//2, f"-{number_of_moves}a")
        elements.insert(len(elements)//2, f"-{number_of_moves}a")
        continue

    if elements[index1] == elements[index2]:
        print(f"Congrats! You have found matching elements - {elements[index1]}!")
        found = elements[index1]
        elements.remove(found)
        elements.remove(found)
    else:
        print("Try again!")

    if not elements:
        print(f"You have won in {number_of_moves} turns!")
        break


