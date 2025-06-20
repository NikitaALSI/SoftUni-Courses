def swap(a, b, _list):
    _list[a], _list[b] = _list[b], _list[a]
    return _list


def multiply(a, b, _list):
    _list[a] *= _list[b]
    return _list


def decrease(_list):
    return list(map(lambda x: x-1, _list))


array_of_int = [int(x) for x in input().split()]

while True:
    cmd = input()
    if cmd == "end":
        print(", ".join(map(str, array_of_int)))
        break

    if cmd.startswith("swap"):
        index1, index2 = list(map(int, cmd.split()[1:]))
        array_of_int = swap(index1, index2, array_of_int)
    elif cmd.startswith("multiply"):
        index1, index2 = list(map(int, cmd.split()[1:]))
        array_of_int = multiply(index1, index2, array_of_int)
    elif cmd.startswith("decrease"):
        array_of_int = decrease(array_of_int)