stock = {}
sold = 0
while (cmd := input()) != "Complete":
    if cmd.startswith("Receive"):
        quantity, food = cmd.split()[1:]
        if int(quantity) <= 0:
            continue
        stock[food] = stock.get(food, 0) + int(quantity)
    elif cmd.startswith("Sell"):
        quantity, food = cmd.split()[1:]
        if food not in stock.keys():
            print(f"You do not have any {food}.")
            continue
        elif stock[food] < int(quantity):
            quantity = stock[food]
            print(f"There aren't enough {food}. You sold the last {stock[food]} of them.")
            stock[food] = 0
        else:
            stock[food] -= int(quantity)
            print(f"You sold {quantity} {food}.")

        sold += int(quantity)
        if stock[food] == 0:
            del stock[food]

for food, quantity in stock.items():
    print(f"{food}: {quantity}")
print(f"All sold: {sold} goods")

