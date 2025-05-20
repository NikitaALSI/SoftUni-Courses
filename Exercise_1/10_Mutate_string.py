string_a = input()
string_b = input()

for change in range(len(string_a)):
    new_string = f"{string_b[:change + 1]}{string_a[change + 1:]}"
    if string_a[change] != string_b[change]:
        print(new_string)
