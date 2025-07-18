dwarfs = []
order_of_input = 0
while (cmd := input()) != "Once upon a time":
    name, color, physics = cmd.split(" <:> ")
    for index, dwarf in enumerate(dwarfs):
        if (dwarf[0], dwarf[1]) == (color, name):
            dwarfs[index] = (color, name, max(int(physics), dwarfs[index][2]), dwarfs[index][3])
            break
    else:
        dwarfs.append((color, name, int(physics), order_of_input))
    order_of_input += 1

color_count = {}
for dwarf in dwarfs:
    color, name, physics, order_of_input = dwarf
    color_count[color] = color_count.get(color, 0) + 1

sorted_dwarf = []
for index, dwarf in enumerate(dwarfs):
    color, name, physics, order_of_input = dwarf
    sorted_dwarf.append((color, color_count[color], name, physics, order_of_input))

sorted_dwarf = sorted(sorted_dwarf, key=lambda x: (-x[3], -x[1], x[4]))

for dwarf in sorted_dwarf:
    color, color_count, name, physics, order_of_input = dwarf
    print(f"({color}) {name} <-> {physics}")






