TICKET = 150
goods = input().split("|")
budget = int(input())
income = 0
new_prices = []

for pack in goods:
    good = pack.split("->")
    ranges = (
        (good[0] == "Clothes" and float(good[1]) <= 50.0) or
        (good[0] == "Shoes" and float(good[1]) <= 35.0) or
        (good[0] == "Accessories" and float(good[1]) <= 20.5)
)
    if ranges and budget - float(good[1]) >= 0:
        budget -= float(good[1])
        new_price = 1.4 * float(good[1])
        new_prices.append(f"{new_price:.2f}")
        income += 0.4 * float(good[1])

print(" ".join(new_prices))
print(f"Profit: {income:.2f}")

if sum(list(map(float, new_prices))) + budget >= TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")
