friends = input().split(", ")

while True:
    cmd = input()
    if cmd == "Report":
        print(f"Blacklisted names: {len(list(filter(lambda x: x == 'Blacklisted', friends)))}\n"
              f"Lost names: {len(list(filter(lambda x: x == 'Lost', friends)))}\n"
              f"{' '.join(friends)}")
        break
    elif cmd.startswith("Blacklist"):
        name = cmd.split()[-1]
        if name in friends:
            friends[friends.index(name)] = "Blacklisted"
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    elif cmd.startswith("Error"):
        index = int(cmd.split()[-1])
        if 0 <= index < len(friends):
            if friends[index] != "Lost" and friends[index] != "Blacklisted":
                print(f"{friends[index]} was lost due to an error.")
                friends[index] = "Lost"
    elif cmd.startswith("Change"):
        index, new_name = cmd.split()[1:]
        if 0 <= int(index) < len(friends):
            print(f"{friends[int(index)]} changed his username to {new_name}.")
            friends[int(index)] = new_name
