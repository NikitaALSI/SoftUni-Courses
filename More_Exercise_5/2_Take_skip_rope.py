hidden_message = [char for char in input()]
number_list = list(filter(lambda x: x.isdigit(), hidden_message))
non_number_list = list(filter(lambda x: not x.isdigit(), hidden_message))

# take_list = list(filter(lambda x: number_list.index(x) % 2 == 0, number_list))
# skip_list = list(filter(lambda x: number_list.index(x) % 2 != 0, number_list))

result_string = []
add = 0
for index, value in enumerate(number_list):
    if index % 2 == 0:
        for i in range(int(value)):
            if i + add < len(non_number_list):
                result_string.append(non_number_list[i+add])
    add += int(value)


print("".join(result_string))