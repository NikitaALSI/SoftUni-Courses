number = int(input())
tank_capacity = 255

for i in range(number):
    water_to_pour = int(input())
    if tank_capacity < water_to_pour:
        print("Insufficient capacity!")
        continue
    else:
        tank_capacity -= water_to_pour

print(255 - tank_capacity)
