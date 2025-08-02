import re

pat = r">>([a-z]+)<<(([0-9])+(\.[0-9]+)*)!([0-9]+)"
total_spend = 0
bought_furniture = []

while (cmd := input()) != "Purchase":
    valid_purchase = re.match(pat, cmd, re.I)
    if valid_purchase:
        bought_furniture.append(valid_purchase.group(1))
        total_spend += float(valid_purchase.group(2)) * int(valid_purchase.group(5))

print("Bought furniture:")
for item in bought_furniture:
    print(item)
print(f"Total money spend: {total_spend:.2f}")
