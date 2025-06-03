numbers = [int(input()) for _ in range(int(input()))]
command = input()

if command == "even":
    filtered_list = [number for number in numbers if number % 2 == 0]
if command == "odd":
    filtered_list = [number for number in numbers if number % 2 != 0]
if command == "negative":
    filtered_list = [number for number in numbers if number < 0]
if command == "positive":
    filtered_list = [number for number in numbers if number >= 0]

print(filtered_list)



