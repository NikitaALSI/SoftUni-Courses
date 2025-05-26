start = int(input())
end = int(input())

for index in range(start, end + 1):
    if index == end + 1:
        print(chr(index))
    else:
        print(chr(index), end=" ")