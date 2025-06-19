pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
max_health = int(input())
while True:
    move = input().split()
    if "Retire" in move:
        print(f"Pirate ship status: {sum(pirate_ship_status)}\n"
              f"Warship status: {sum(warship_status)}")
        break
    elif "Fire" in move:
        if int(move[1]) in range(len(warship_status)):
            warship_status[int(move[1])] -= int(move[2])
            if warship_status[int(move[1])] <= 0:
                print("You won! The enemy ship has sunken.")
                break
    elif "Defend" in move:
        if int(move[1]) in range(len(pirate_ship_status)) and int(move[2]) in range(len(pirate_ship_status)):
            sunken = False
            for section in range(int(move[1]), int(move[2]) + 1):
                pirate_ship_status[section] -= int(move[3])
                if pirate_ship_status[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    sunken = True
                    break
            if sunken:
                break
    elif "Repair" in move:
        if int(move[1]) in range(len(pirate_ship_status)):
            pirate_ship_status[int(move[1])] += int(move[2])
            if pirate_ship_status[int(move[1])] > max_health:
                pirate_ship_status[int(move[1])] = max_health
    elif "Status" in move:
        print(f"{len(list((filter(lambda x: x < 0.2 * max_health, pirate_ship_status))))} sections need repair.")
