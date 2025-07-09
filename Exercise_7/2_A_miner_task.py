resources = {}

while (material := input()) != "stop":
    quantity = int(input())
    resources[material] = resources.get(material, 0) + quantity


for mat, count in resources.items():
    print(f"{mat} -> {count}")