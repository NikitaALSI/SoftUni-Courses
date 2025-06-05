def total_price(beverage: str, quantity: int):
    prices = {
        "coffee": quantity * 1.5,
        "water": quantity * 1.00,
        "coke": quantity * 1.40,
        "snacks": quantity * 2.00,
    }
    return f"{prices[beverage]:.2f}"


item = input()
quantity = int(input())
print(total_price(item, quantity))
