initial_loot = input().split("|")

while True:
    action = input().split()
    if "Yohoho!" in action:
        if initial_loot:
            print(f"Average treasure gain: {sum(map(lambda x: len(x), initial_loot)) / len(initial_loot):.2f} pirate credits.")
        else:
            print("Failed treasure hunt.")
        break
    elif "Loot" in action:
        for item in action[1::]:
            if item not in initial_loot:
                initial_loot.insert(0, item)
    elif "Drop" in action:
        if int(action[1]) in range(len(initial_loot)):
            initial_loot.append(initial_loot.pop(int(action[1])))
    elif "Steal" in action:
        stolen_items = []
        for item in range(min(len(initial_loot), int(action[1]))):
            stolen_items.append(initial_loot.pop())
        print(", ".join(reversed(stolen_items)))