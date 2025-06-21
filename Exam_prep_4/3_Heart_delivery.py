neighborhood = [int(x) for x in input().split("@")]
jump = 0
while True:
    cmd = input()
    if cmd == "Love!":
        print(f"Cupid's last position was {jump}.")
        if all(map(lambda x: x == 0, neighborhood)):
            print("Mission was successful.")
        else:
            print(f"Cupid has failed {len(list(filter(lambda x: x != 0, neighborhood)))} places.")
        break
    else:
        jump += int(cmd.split()[-1])
        if jump >= len(neighborhood):
            jump = 0
        if neighborhood[jump] != 0:
            neighborhood[jump] -= 2
            if neighborhood[jump] == 0:
                print(f"Place {jump} has Valentine's day.")
        else:
            print(f"Place {jump} already had Valentine's day.")