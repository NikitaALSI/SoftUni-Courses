number_of_heroes = int(input())
heroes = {}

for _ in range(number_of_heroes):
    name, HP, MP = input().split()
    heroes[name] = {"HP": int(HP), "MP": int(MP)}

while (cmd := input()) != "End":
    if cmd.startswith("CastSpell"):
        name, MP_needed, spell_name = cmd.split(" - ")[1:]
        if heroes[name]["MP"] >= int(MP_needed):
            heroes[name]["MP"] -= int(MP_needed)
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['MP']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif cmd.startswith("TakeDamage"):
        name, damage, attacker = cmd.split(" - ")[1:]
        heroes[name]["HP"] -= int(damage)
        if heroes[name]["HP"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")
        else:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")
    elif cmd.startswith("Recharge"):
        name, amount = cmd.split(" - ")[1:]
        new_MP = min(heroes[name]["MP"] + int(amount), 200)
        recovered = new_MP - heroes[name]["MP"]
        heroes[name]["MP"] = new_MP
        print(f"{name} recharged for {recovered} MP!")
    elif cmd.startswith("Heal"):
        name, amount = cmd.split(" - ")[1:]
        new_HP = min(heroes[name]["HP"] + int(amount), 100)
        recovered = new_HP - heroes[name]["HP"]
        heroes[name]["HP"] = new_HP
        print(f"{name} healed for {recovered} HP!")
for hero in heroes:
    print(f"{hero}\n"
          f"  HP: {heroes[hero]['HP']}\n"
          f"  MP: {heroes[hero]['MP']}")
