stops = input()

while (cmd := input()) != "Travel":
    if cmd.startswith("Add"):
        index, string = cmd.split(":")[1:]
        if int(index) in range(len(stops)):
            stops = stops[:int(index)] + string + stops[int(index):]
        print(stops)
    elif cmd.startswith("Remove"):
        start, end = cmd.split(":")[1:]
        if int(start) in range(len(stops)) and int(end) in range(len(stops)):
            stops = stops[:int(start)] + stops[int(end)+1:]
        print(stops)
    elif cmd.startswith("Switch"):
        old, new = cmd.split(":")[1:]
        if old in stops:
            stops = stops.replace(old, new)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")