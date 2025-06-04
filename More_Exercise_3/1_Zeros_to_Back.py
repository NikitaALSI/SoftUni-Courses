string_of_integers = list(map(int, input().split(", ")))

for element in string_of_integers:
    if element == 0:
        string_of_integers.remove(0)
        string_of_integers.append(0)

print(string_of_integers)