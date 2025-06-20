total_price = 0
TAX = 0.2
DISCOUNT = 0.1

while True:
    price = input()
    if price == "special" or price == "regular":
        tax_amount = TAX * total_price
        total_price_with_tax = (1 + TAX) * total_price
        if price == "special":
            total_price_with_tax_discounted = (1 - DISCOUNT) * total_price_with_tax

        if total_price == 0:
            print("Invalid order!")
            break

        print(f"Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {total_price:.2f}$\n"
              f"Taxes: {tax_amount:.2f}$\n"
              "-----------\n"
              f"Total price: {(total_price_with_tax_discounted if price == 'special' else total_price_with_tax):.2f}$")
        break
    if float(price) < 0:
        print("Invalid price!")
    else:
        total_price += float(price)
