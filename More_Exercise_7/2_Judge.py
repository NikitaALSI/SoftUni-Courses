results = {}
while (cmd := input()) != "no more time":
    user, contest, points = cmd.split(" -> ")
    if contest not in results.keys():
        results[contest] = {user: int(points)}
    elif user not in results[contest]:
        results[contest][user] = int(points)
    else:
        results[contest][user] = max(results[contest][user], int(points))

for contest in results.keys():
    print(f"{contest}: {len(results[contest])} participants")
    n = 1
    for user, points in dict(sorted(results[contest].items(), key=lambda x: (-x[1], x[0]))).items():
        print(f"{n}. {user} <::> {points}")
        n += 1

total_points = {}
for contest in results.values():
    for user, points in contest.items():
        total_points[user] = total_points.get(user, 0)+points

print("Individual standings:")
n = 1
for user, points in dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0]))).items():
    print(f"{n}. {user} -> {points}")
    n += 1