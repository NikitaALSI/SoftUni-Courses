number_of_letters = int(input())
for a in range(97, 97 + number_of_letters):
    for b in range(97, 97 + number_of_letters):
        for c in range(97, 97 + number_of_letters):
            print(f"{chr(a)}{chr(b)}{chr(c)}")