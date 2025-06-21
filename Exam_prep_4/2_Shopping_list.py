def urgent(thing, _list):
    if thing not in _list:
        _list.insert(0, thing)
    return _list


def unnecessary(thing, _list):
    if thing in _list:
        _list.remove(thing)
    return _list


def correct(thing1, thing2, _list):
    if thing1 in _list:
        _list[_list.index(thing1)] = thing2
    return _list


def rearrange(thing, _list):
    if thing in _list:
        _list.append(_list.pop(_list.index(thing)))
    return _list


def get_cmd(string):
    return string.split()[1:]


shopping_list = input().split("!")

while True:
    cmd = input()
    if cmd == "Go Shopping!":
        print(f"{', '.join(shopping_list)}")
        break

    if cmd.startswith("Urgent"):
        item = get_cmd(cmd)[0]
        shopping_list = urgent(item, shopping_list)
    elif cmd.startswith("Unnecessary"):
        item = get_cmd(cmd)[0]
        shopping_list = unnecessary(item, shopping_list)
    elif cmd.startswith("Correct"):
        item1, item2 = get_cmd(cmd)
        shopping_list = correct(item1, item2, shopping_list)
    elif cmd.startswith("Rearrange"):
        item = get_cmd(cmd)[0]
        shopping_list = rearrange(item, shopping_list)
