from math import ceil

employee_capacity = [int(input()) for _ in range(3)]
students = int(input())

total_time = ceil(students / sum(employee_capacity))
break_time = total_time // 3
if total_time % 3 == 0:
    break_time -= 1
total_time += (break_time if break_time > 0 else 0)

print(f"Time needed: {total_time}h.")
