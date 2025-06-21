def collect(thing, _list):
    if thing not in _list:
        _list.append(thing)
    return _list


def drop(thing, _list):
    if thing in _list:
        _list.remove(thing)
    return _list


def combine(thing1, thing2, _list):
    if thing1 in _list:
        _list.insert(_list.index(thing1) + 1, thing2)
    return _list


def renew(thing, _list):
    if thing in _list:
        _list.append(_list.pop(_list.index(thing)))
    return _list


collection = input().split(", ")
while True:
    cmd = input()
    if cmd == "Craft!":
        print(", ".join(collection))
        break

    elif cmd.startswith("Collect"):
        item = cmd.split(" - ")[-1]
        collection = collect(item, collection)
    elif cmd.startswith("Drop"):
        item = cmd.split(" - ")[-1]
        collection = drop(item, collection)
    elif cmd.startswith("Combine"):
        item1, item2 = cmd.split(" - ")[-1].split(":")
        collection = combine(item1, item2, collection)
    elif cmd.startswith("Renew"):
        item = cmd.split(" - ")[-1]
        collection = renew(item, collection)
