N = int(input())
total_price = 0

for order in range(N):
    capsule_price = float(input())
    days = int(input())
    capsule_quantity = int(input())

    if (0.01 <= capsule_price <= 100.0
            and days in range(1, 32)
            and capsule_quantity in range(1, 2001)):
        order_price = capsule_price * days * capsule_quantity
        print(f"The price for the coffee is: ${order_price:.2f}")
        total_price += order_price

print(f"Total: ${total_price:.2f}")