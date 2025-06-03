energy = 100
coins = 100
day_order = input().split("|")

for order in day_order:
    action = order.split("-")
    if action[0] == "rest":
        energy += int(action[1])
        if energy > 100:
            print(f"You gained {100 - energy + int(action[1])} energy.")
            energy = 100
        else:
            print(f"You gained {int(action[1])} energy.")
        print(f"Current energy: {energy}.")
    elif action[0] == "order":
        if energy - 30 >= 0:
            coins += int(action[1])
            energy -= 30
            print(f"You earned {int(action[1])} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")
    else:
        if coins >= int(action[1]):
            coins -= int(action[1])
            print(f"You bought {action[0]}.")
        else:
            print(f"Closed! Cannot afford {action[0]}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
