pool = {}

while (cmd := input()) != "Season end":
    if "->" in cmd:
        player, position, skill = cmd.split(" -> ")
        if player not in pool.keys():
            pool[player] = {position: int(skill)}
        elif position not in pool[player]:
            pool[player][position] = int(skill)
        else:
            pool[player][position] = max(int(skill), pool[player][position])

    else:
        player_1, player_2 = cmd.split(" vs ")
        if player_1 not in pool.keys() or player_2 not in pool.keys():
            continue
        else:
            match = False
            for position_1 in pool[player_1].keys():
                if match:
                    break
                for position_2 in pool[player_2].keys():
                    if position_1 == position_2:
                        match = True
                        if sum(pool[player_1].values()) > sum(pool[player_2].values()):
                            del pool[player_2]
                        elif sum(pool[player_1].values()) < sum(pool[player_2].values()):
                            del pool[player_1]
                        break

total_points = dict(sorted({player: sum(pool[player].values()) for player in pool.keys()}.items(), key=lambda x: (-x[1], x[0])))

for player in total_points.keys():
    print(f"{player}: {total_points[player]} skill")
    sorted_revision = dict(sorted({position: pool[player][position] for position in pool[player].keys()}.items(), key=lambda x: (-x[1], x[0])))
    for position, skill in sorted_revision.items():
        print(f"- {position} <::> {skill}")


