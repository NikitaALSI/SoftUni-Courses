divider = int(input())
boundary = int(input())

for i in range(boundary, divider, -1):
    if i % divider == 0:
        print(i)
        break