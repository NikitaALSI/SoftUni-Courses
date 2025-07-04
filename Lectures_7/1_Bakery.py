food_quantities = input().split()
bakery = {key: int(value) for key, value in zip([x for x in food_quantities if not x.isdigit()], [x for x in food_quantities if x.isdigit()])}
print(bakery)
