number_of_dragons = int(input())
dragons = {}
for _ in range(number_of_dragons):
    cmd = input().split()
    _type, name = cmd[:2]
    damage, health, armour = ((45 if cmd[2] == "null" else int(cmd[2])),
                              (250 if cmd[3] == "null" else int(cmd[3])),
                              (10 if cmd[4] == "null" else int(cmd[4])))
    dragons[_type] = dragons.get(_type, {})
    dragons[_type][name] = (damage, health, armour)

for _type in dragons.keys():
    average = [0,0,0]
    for damage, health, armour in dragons[_type].values():
        average[0] += damage
        average[1] += health
        average[2] += armour
    average = list(map(lambda x: x/ len(dragons[_type].keys()), average))
    print(f"{_type}::({average[0]:.2f}/{average[1]:.2f}/{average[2]:.2f})")
    sorted_type = dict(sorted(dragons[_type].items()))
    for name in sorted_type.keys():
        damage, health, armour = sorted_type[name]
        print(f"-{name} -> damage: {damage}, health: {health}, armor: {armour}")

