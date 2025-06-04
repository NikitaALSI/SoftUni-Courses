times = list(map(int, input().split(" ")))
left = times[:int(len(times)/2)]
right = times[int(len(times)/2 + 1):]
left_time = 0
right_time = 0
winner = ""

for time in left:
    if time == 0:
        left_time *= 0.8
    else:
        left_time += time

for time in right[::-1]:
    if time == 0:
        right_time *= 0.8
    else:
        right_time += time

if left_time < right_time:
    winner = "left"
else:
    winner = "right"

print(f"The winner is {winner} with total time: {min(left_time, right_time):.1f}")