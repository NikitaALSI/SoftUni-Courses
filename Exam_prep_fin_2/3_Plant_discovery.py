rows = int(input())

plant_book = {}
for _ in range(rows):
    plant, rarity = input().split("<->")
    plant_book[plant] = {"rarity": float(rarity)}

while (cmd := input()) != "Exhibition":
    action, info = cmd.split(": ")
    if action == "Rate":
        plant, rating = info.split(" - ")
        if plant not in plant_book.keys():
            print("error")
            continue
        if "rating" not in plant_book[plant].keys():
            plant_book[plant]["rating"] = [float(rating)]
        else:
            plant_book[plant]["rating"].append(float(rating))
    elif action == "Update":
        plant, rarity = info.split(" - ")
        if plant not in plant_book.keys():
            print("error")
            continue
        plant_book[plant]["rarity"] = int(rarity)
    elif action == "Reset":
        plant = info
        if plant not in plant_book.keys():
            print("error")
            continue
        del plant_book[plant]["rating"]

print("Plants for the exhibition:")
for plant, info in plant_book.items():
    print(f"- {plant}; Rarity: {int(info['rarity'])}; Rating: {sum(info['rating'])/len(info['rating']) if 'rating' in info.keys() else 0:.2f}")