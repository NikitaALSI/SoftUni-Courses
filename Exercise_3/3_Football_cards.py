team_A = [f"A-{i}" for i in range(1, 12)]
team_B = [f"B-{i}" for i in range(1, 12)]

sentenced = input().split(" ")

if sentenced[0] != "":
    for player in sentenced:
        if player[0] == "A":
            if player in team_A:
                team_A.remove(player)
        elif player[0] == "B":
            if player in team_B:
                team_B.remove(player)
        if len(team_A) < 7 or len(team_B) < 7:
            break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if len(team_A) < 7 or len(team_B) < 7:
    print("Game was terminated")
