rounding = lambda lst: list(map(round, map(float, lst.split(" "))))

print(rounding(input()))