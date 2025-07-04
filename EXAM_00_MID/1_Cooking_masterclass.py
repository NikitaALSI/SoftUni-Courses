from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

expenses = students * (flour_price + 10 * egg_price + apron_price)
expenses -= (students // 5) * flour_price
expenses += ceil(0.2 * students) * apron_price

if expenses <= budget:
    print(f"Items purchased for {expenses:.2f}$.")
else:
    print(f"{expenses - budget:.2f}$ more needed.")
