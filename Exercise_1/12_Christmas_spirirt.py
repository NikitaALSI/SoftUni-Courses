quantity = int(input())
days_till_Christmas = int(input())

ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLAND = 3
TREE_LIGHTS = 15

budget = 0
total_spirit = 0
for day in range(1, days_till_Christmas + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += ORNAMENT_SET * quantity
        total_spirit += 5
    if day % 3 == 0:
        budget += (TREE_SKIRT + TREE_GARLAND) * quantity
        total_spirit += 3 + 10
    if day % 5 == 0:
        budget += TREE_LIGHTS * quantity
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        budget += TREE_SKIRT + TREE_GARLAND + TREE_LIGHTS
        total_spirit -= 20

if days_till_Christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
