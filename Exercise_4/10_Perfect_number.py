def perfect_number_validator(some_number: int) -> str:
    sum_of_divisors = 0
    for i in range(1, some_number):
        if some_number % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."


print(perfect_number_validator(int(input())))