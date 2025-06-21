food = float(input())
hay = float(input())
cover = float(input())

guinea_pig_weight = float(input())

for day in range(1, 31):
    food -= 0.3
    if day % 2 == 0:
        hay -= 0.05 * food
    if day % 3 == 0:
        cover -= guinea_pig_weight/3

    if any(map(lambda x: round(x, 2) <= 0.0, [food, hay, cover])):
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")