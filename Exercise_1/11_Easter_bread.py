EGGS = 1
FLOUR = 1
MILK = 0.25

budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price

one_loaf_price = flour_price + eggs_price + MILK * milk_price

colored_eggs = 0
number_of_loaves = 0

while budget > one_loaf_price:
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2
    budget -= one_loaf_price

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")