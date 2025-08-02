import re

total = 0
customer_pattern = r"^%([A-Z][a-z]+)%.*<(\w+)>.*\|(\d+)\|\D*(\d+\.*\d+)\$$"
while (customer := input()) != "end of shift":
    found = re.match(customer_pattern, customer)
    if found:
        name, product, count, price = found.groups()
        total += int(count)*float(price)
        print(f"{name}: {product} - {int(count)*float(price):.2f}")
print(f"Total income: {total:.2f}")