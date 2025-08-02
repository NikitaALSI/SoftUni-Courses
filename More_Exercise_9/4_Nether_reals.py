import re


the_book = {}
names = [name.strip() for name in input().split(",")]
health_pat = r'[^0-9\+\-\*\/\.]'
damage_pat = r'([\-\+]?\d+(\.\d+)*)'
damage_special_pat = r'[\*\/]'

for name in names:
    health = sum([ord(char) for char in re.findall(health_pat, name)])

    damage = sum([float(dig.group(1)) for dig in re.finditer(damage_pat, name)])
    for special in re.findall(damage_special_pat, name):
        if special == "*":
            damage *= 2
        else:
            damage /= 2
    the_book[name] = {"health": health, "damage": damage}


the_book = dict((sorted(the_book.items(), key=lambda x: x[0])))
for demon in the_book.keys():
    health, damage = the_book[demon].values()
    print(f"{demon} - {health} health, {damage:.2f} damage")