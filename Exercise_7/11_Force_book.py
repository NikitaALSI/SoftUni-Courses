force_sides_user = {}
users = []

while (cmd := input()) != "Lumpawaroo":
    if "|" in cmd:
        force, user = cmd.split(" | ")
        if user not in users:
            force_sides_user[force] = force_sides_user.get(force, [])
            force_sides_user[force].append(user)
            users.append(user)
        elif user in users:
            continue

    elif "->" in cmd:
        user, force = cmd.split(" -> ")
        if user in users:
            for side, parts in force_sides_user.items():
                if user in parts:
                    force_sides_user[side].remove(user)
                    force_sides_user[force] = force_sides_user.get(force, [])
                    force_sides_user[force].append(user)
                    break
        elif user not in users:
            force_sides_user[force] = force_sides_user.get(force, [])
            force_sides_user[force].append(user)
            users.append(user)

        print(f"{user} joins the {force} side!")

for side in force_sides_user:
    if force_sides_user[side]:
        print(f"Side: {side}, Members: {len(force_sides_user[side])}")
        for user in force_sides_user[side]:
            print(f"! {user}")
