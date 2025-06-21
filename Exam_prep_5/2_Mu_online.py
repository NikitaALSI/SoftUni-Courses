MAX_HEALTH = 100
health = MAX_HEALTH
bitcoins = 0

dungeons = [[i.split()[0], int(i.split()[1])] for i in input().split("|")]
for number, room in enumerate(dungeons):
    if room[0] == "potion":
        heal = min(room[1], MAX_HEALTH - health)
        print(f"You healed for {heal} hp.")
        health += heal
        print(f"Current health: {health} hp.")
    elif room[0] == "chest":
        bitcoins += room[1]
        print(f"You found {room[1]} bitcoins.")
    else:
        health -= room[1]
        if health > 0:
            print(f"You slayed {room[0]}.")
        else:
            print(f"You died! Killed by {room[0]}.")
            print(f"Best room: {number + 1}")
            break
else:
    print(f"You've made it!\n"
          f"Bitcoins: {bitcoins}\n"
          f"Health: {health}")
