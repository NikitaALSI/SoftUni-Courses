food_quantities = input().split()
stock = {key: int(value) for key, value in zip([x for x in food_quantities if not x.isdigit()], [x for x in food_quantities if x.isdigit()])}
to_check = input().split()
for item in to_check:
    if item in stock:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")