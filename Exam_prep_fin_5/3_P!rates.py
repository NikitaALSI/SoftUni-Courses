targets = {}

while (target := input()) != "Sail":
    city, population, gold = target.split("||")
    if city not in targets:
        targets[city] = {"population": int(population), "gold": int(gold)}
    else:
        targets[city]["population"] += int(population)
        targets[city]["gold"] += int(gold)

while (event := input()) != "End":
    if event.startswith("Plunder"):
        city, people, gold = event.split("=>")[1:]
        targets[city]["population"] -= int(people)
        targets[city]["gold"] -= int(gold)
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if any(list(map(lambda x: x == 0, targets[city].values()))):
            del targets[city]
            print(f"{city} has been wiped off the map!")
    elif event.startswith("Prosper"):
        city, gold = event.split("=>")[1:]
        if gold.startswith("-"):
            print("Gold added cannot be a negative number!")
        else:
            targets[city]["gold"] += int(gold)
            print(f"{gold} gold added to the city treasury. {city} now has {targets[city]['gold']} gold.")

if targets:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    for target in targets:
        people, gold = targets[target]["population"], targets[target]["gold"]
        print(f"{target} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")