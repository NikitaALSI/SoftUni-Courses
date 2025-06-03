fires = input().split("#")
water = int(input())
effort = 0
total_fire = 0
cells = []
for cell in fires:
    fire = cell.split(" = ")
    ranges = (
        (fire[0] == "High" and int(fire[1]) in range(81, 126)) or
        (fire[0] == "Medium" and int(fire[1]) in range(51, 81)) or
        (fire[0] == "Low" and int(fire[1]) in range(1, 51))
    )
    if ranges:
        if water - int(fire[1]) >= 0:
            water -= int(fire[1])
            total_fire += int(fire[1])
            effort += int(fire[1]) * 0.25
            cells.append(fire[1])
        else:
            continue

print(f"Cells:")
if cells:
    for cell in cells:
        print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")