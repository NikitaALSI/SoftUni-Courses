from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_bonus_attendance = 0

for i in range(number_of_students):
    attendance = int(input())
    total_bonus = attendance / number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_bonus_attendance = attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_bonus_attendance} lectures.")