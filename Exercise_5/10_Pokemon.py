def caught(i, some_list):
    new_list = list(map(lambda x: x + some_list[i] if x <= some_list[i] else x - some_list[i], some_list))
    return new_list


pokemons = list(map(int, input().split()))
removed = []

while pokemons:
    index = int(input())
    if index < 0:
        removed.append(pokemons[0])
        pokemons = caught(0, pokemons)
        pokemons.pop(0)
        pokemons.insert(0, pokemons[-1])
    elif index >= len(pokemons):
        removed.append(pokemons[-1])
        pokemons = caught(-1, pokemons)
        pokemons.pop(-1)
        pokemons.append(pokemons[0])
    else:
        removed.append(pokemons[index])
        pokemons = caught(index, pokemons)
        pokemons.pop(index)
        
print(sum(removed))