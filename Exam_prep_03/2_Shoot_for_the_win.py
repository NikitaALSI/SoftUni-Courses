target_values = [int(x) for x in input().split()]

while True:
    cmd = input()
    if cmd == "End":
        print(f"Shot targets: {len(list(filter(lambda x: x == -1, target_values)))} -> {' '.join([str(x) for x in target_values])}")
        break

    index = int(cmd)
    if index in range(len(target_values)) and target_values[index] != -1:
        for i in range(len(target_values)):
            if target_values[i] != -1 and target_values[i] > target_values[index] and i != index:
                target_values[i] -= target_values[index]
            elif target_values[i] != -1 and target_values[i] <= target_values[index] and i != index:
                target_values[i] += target_values[index]
            else:
                continue
        target_values[index] = -1
