target_values = [int(x) for x in input().split()]

while True:
    cmd = input()

    if cmd == "End":
        print(f"{'|'.join([str(x) for x in target_values])}")
        break

    if cmd.startswith("Shoot"):
        index, power = [int(x) for x in cmd.split()[1:]]
        if index in range(len(target_values)):
            target_values[index] -= power
            if target_values[index] <= 0:
                target_values.pop(index)
        else:
            continue

    elif cmd.startswith("Add"):
        index, value = [int(x) for x in cmd.split()[1:]]
        if index in range(len(target_values)):
            target_values.insert(index, value)
        else:
            print("Invalid placement!")
            continue

    elif cmd.startswith("Strike"):
        index, radius = [int(x) for x in cmd.split()[1:]]
        if (radius + index) in range(len(target_values)) and (index - radius) in range(len(target_values)):
            index -= radius
            for j in range((2 * radius) + 1):
                target_values.pop(index)
        else:
            print("Strike missed!")
            continue
