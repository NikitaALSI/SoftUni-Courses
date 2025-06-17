list_of_numbers = list(map(int, input().split(", ")))


def classify_numbers(numbers):
    positive = [str(number) for number in list_of_numbers if number >= 0]
    negative = [str(number) for number in list_of_numbers if number < 0]
    even = [str(number) for number in list_of_numbers if number % 2 == 0]
    odd = [str(number) for number in list_of_numbers if number % 2 != 0]
    return (f"Positive: {', '.join(positive)}\n"
            f"Negative: {', '.join(negative)}\n"
            f"Even: {', '.join(even)}\n"
            f"Odd: {', '.join(odd)}")


print(classify_numbers(list_of_numbers))
