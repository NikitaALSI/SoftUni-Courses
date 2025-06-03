amounts = input().split(", ")
beggars = int(input())

amounts_per_beggar = []

for beggar in range(beggars):
    amount = 0
    for value in amounts[beggar::beggars]:
        amount += int(value)
    amounts_per_beggar.append(amount)

print(amounts_per_beggar)