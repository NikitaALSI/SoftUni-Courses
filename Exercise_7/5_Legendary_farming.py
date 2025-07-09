materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
legendary_item = False
while True:
    items = input().split()
    for index in range(0, len(items), 2):
        item = items[index + 1].lower()
        quantity = int(items[index])
        materials[item] = materials.get(item, 0) + quantity

        if materials["shards"] >= 250:
            print("Shadowmourne obtained!")
            materials["shards"] -= 250
            legendary_item = True
            break
        elif materials["fragments"] >= 250:
            print("Valanyr obtained!")
            materials["fragments"] -= 250
            legendary_item = True
            break
        elif materials["motes"] >= 250:
            print("Dragonwrath obtained!")
            materials["motes"] -= 250
            legendary_item = True
            break
    if legendary_item:
        break

for material, quantity in materials.items():
    print(f"{material}: {quantity}")
