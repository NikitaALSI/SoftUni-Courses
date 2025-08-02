import re


inquiries = input()
food_pat = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
foods = re.findall(food_pat, inquiries)
total_calories = sum(map(lambda x: int(x[5]), foods))
print(f"You have food to last you for: {total_calories//2000} days!")
for food in foods:
    name = food[1]
    date = food[3]
    calories = food[5]
    print(f"Item: {name}, Best before: {date}, Nutrition: {calories}")
