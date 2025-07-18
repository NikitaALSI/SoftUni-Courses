contests ={}
submissions = {}
while (cmd := input()) != "end of contests":
    contest, password = cmd.split(":")
    contests[contest] = password

while (cmd := input()) != "end of submissions":
    contest, password, user, points = cmd.split("=>")
    if contest in contests.keys() and contests[contest] == password:
        if user not in submissions.keys():
            submissions[user] = {contest: int(points)}
        elif contest not in submissions[user]:
            submissions[user][contest] = int(points)
        else:
            submissions[user][contest] = max(submissions[user][contest], int(points))


all_points = {user: sum(submissions[user].values()) for user in submissions.keys()}
best_candidate = ""
max_points = 0
for user, points in all_points.items():
    if points > max_points:
        best_candidate = user
        max_points = points

print(f"Best candidate is {best_candidate} with total {max_points} points.\nRanking:")
users = sorted(submissions.keys())
for user in users:
    print(f"{user}")
    for contest, points in dict(sorted(submissions[user].items(), key=lambda x: x[1], reverse=True)).items():
        print(f"#  {contest} -> {points}")