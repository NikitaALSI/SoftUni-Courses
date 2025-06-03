integers = input().split()
integers = list(map(int, integers))
to_remove = int(input())

for _ in range(to_remove):
    smallest = min(integers)
    integers.remove(smallest)

integers = list(map(str, integers))
print(", ".join(integers))