wagons = [0] * int(input())

while True:
    command = input().split()
    if "End" in command:
        print(wagons)
        break

    elif "add" in command:
        wagons[-1] += int(command[1])
    elif "insert" in command:
        wagons[int(command[1])] += int(command[-1])
    elif "leave" in command:
        wagons[int(command[1])] -= int(command[-1])