def order_by_decades(list_of_numbers: list):
    number_of_groups = max(list_of_numbers) // 10 if max(list_of_numbers) % 10 == 0 else (max(list_of_numbers) // 10) + 1
    message = ""
    for group in range(1, number_of_groups + 1):
        message += f"Group of {group}0's: {[number for number in list_of_numbers if (group - 1)*10 < number <= group * 10]}\n"
    return message


sequence_of_numbers = list(map(int, input().split(", ")))
print(order_by_decades(sequence_of_numbers))