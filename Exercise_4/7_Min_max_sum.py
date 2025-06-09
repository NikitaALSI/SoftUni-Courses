def min_max_sum(digits_as_string: str) -> str:
    digits = list(map(int, digits_as_string.split(" ")))
    return (f"The minimum number is {min(digits)}\n"
            f"The maximum number is {max(digits)}\n"
            f"The sum number is: {sum(digits)}")


digit = input()
print(min_max_sum(digit))