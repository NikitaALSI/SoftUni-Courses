wins = 0
initial_energy = int(input())

while True:
    cmd = input()

    if cmd == "End of battle":
        print(f"Won battles: {wins}. Energy left: {initial_energy}")
        break

    distance = int(cmd)
    if initial_energy - distance >= 0:
        wins += 1
        initial_energy -= distance
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {initial_energy} energy")
        break

    if wins % 3 == 0:
        initial_energy += wins

