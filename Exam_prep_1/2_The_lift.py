MAX_PEOPLE_FOR_CABIN = 4
people_waiting = int(input())
lift_cabins = list(map(int, input().split()))

index = 0
while True:
    if not people_waiting and any(map(lambda x: x < 4, lift_cabins)):
        print(f"The lift has empty spots!\n"
              f"{' '.join(map(str, lift_cabins))}")
        break
    elif not people_waiting:
        print(f"{' '.join(map(str, lift_cabins))}")
        break

    if index > len(lift_cabins) - 1 and people_waiting:
        print(f"There isn't enough space! {people_waiting} people in a queue!\n"
              f"{' '.join(map(str, lift_cabins))}")
        break

    if lift_cabins[index] < 4:
        lift_cabins[index] += 1
        people_waiting -= 1
    else:
        index += 1




