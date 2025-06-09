def palindrome_validation_list(digits: str):
    valid = digits.split(", ")
    return map(lambda x: x == x[::-1], valid)


for i in palindrome_validation_list(input()):
    print(i)