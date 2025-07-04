stock = {}

while (product := input()) != "statistics":
    item, qty = product.split(": ")
    stock[item] = stock.get(item, 0) + int(qty)
else:
    print(f"Products in stock:", end="")
    for item, qty in stock.items():
        print(f"\n- {item}: {qty}", end="")
    print("\n", end="")
    print(f"Total Products: {len(stock.keys())}")
    print(f"Total Quantity: {sum(stock.values())}")