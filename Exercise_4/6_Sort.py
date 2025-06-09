def sort_string(digits: str) -> list:
    my_list = map(int, digits.split(" "))
    return sorted(my_list)


digit = input()
print(sort_string(digit))