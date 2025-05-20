n = int(input())

for i in range(n):
    string = input()

    for char in string:
        if char in ",._":
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")