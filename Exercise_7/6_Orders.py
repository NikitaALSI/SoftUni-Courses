products = {}

while (product := input()) != "buy":
    item, price, quantity = product.split()
    if not products.get(item):
        products[item] = [float(price), int(quantity)]
    else:
        products[item][0] = float(price)
        products[item][1] += int(quantity)

for product, total in products.items():
    print(f"{product} -> {total[0]*total[1]:.2f}")
