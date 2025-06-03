budget = int(input())

while budget > 0:
    single_price = input()
    if single_price == "End":
        print("You bought everything needed.")
        break

    budget -= int(single_price)
else:
    print("You went in overdraft!")