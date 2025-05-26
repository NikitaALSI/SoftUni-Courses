number_of_snowballs = int(input())
highest_value = 0
highest_weight = 0
highest_time = 0
highest_quality = 0

for snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = int((weight / time) ** quality)
    if value >= highest_value:
        highest_value = value
        highest_weight = weight
        highest_time = time
        highest_quality = quality

print(f"\033[91m{highest_weight}\033[00m : {highest_time} = {highest_value} ({highest_quality})")