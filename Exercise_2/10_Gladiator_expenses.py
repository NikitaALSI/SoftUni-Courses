loses = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet = loses // 2
sword = loses // 3
shield = loses // 6
armor = loses // 12

expenses = (helmet * helmet_price +
            sword * sword_price +
            shield * shield_price +
            armor * armor_price)
print(f"Gladiator expenses: {expenses:.2f} aureus")
