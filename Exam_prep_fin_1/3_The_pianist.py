def add(some_dict, name, author, octav):
    if name not in some_dict.keys():
        some_dict[name] = {"composer": author, "key": octav}
        print(f"{name} by {author} in {octav} added to the collection!")
    else:
        print(f"{name} is already in the collection!")
    return some_dict


def remove(some_dict, name):
    if name in some_dict.keys():
        del some_dict[name]
        print(f"Successfully removed {name}!")
    else:
        print(f"Invalid operation! {name} does not exist in the collection.")
    return some_dict


def change(some_dict, name, octave):
    if name in some_dict.keys():
        some_dict[name]["key"] = octave
        print(f"Changed the key of {name} to {octave}!")
    else:
        print(f"Invalid operation! {name} does not exist in the collection.")
    return some_dict


collection = {}

initial_pieces = int(input())

for _ in range(initial_pieces):
    piece, composer, key = input().split("|")
    collection[piece] = {"composer": composer, "key": key}

while (cmd := input()) != "Stop":
    if cmd.startswith("Add"):
        piece, composer, key = cmd.split("|")[1:]
        collection = add(collection, piece, composer, key)
    elif cmd.startswith("Remove"):
        piece = cmd.split("|")[-1]
        collection = remove(collection, piece)
    elif cmd.startswith("Change"):
        piece, key = cmd.split("|")[1:]
        collection = change(collection, piece, key)

for piece in collection.keys():
    composer = collection[piece]["composer"]
    key = collection[piece]["key"]
    print(f"{piece} -> Composer: {composer}, Key: {key}")