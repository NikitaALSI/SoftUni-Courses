def merge(start, stop, some_list):
    start_index = max(start + 1, 1)
    stop_index = min(stop + 1, len(some_list))

    for i in range(start_index, stop_index):
        some_list[start_index - 1] += some_list[i]
        some_list[i] = ""

    return [element for element in some_list if element != ""]


def divide(index, partition, some_list):
    partitioned = []
    part_length = (len(some_list[index]) // partition)

    start = 0
    stop = part_length

    for i in range(partition):
        partitioned.append(some_list[index][start:stop])
        start = stop

        if i != partition - 2:
            # here we change the start and stop indexes of the last parts [-1] in the irritation of the previous [-2]
            stop += part_length
        else:
            stop = len(some_list[index])

    new_list = some_list[:index] + partitioned + some_list[index+1:]
    return new_list


list_of_strings = input().split()
while True:
    command = input().split()
    if "3:1" in command:
        print(" ".join(list_of_strings))
        break
    elif "merge" in command:
        list_of_strings = merge(int(command[1]), int(command[2]), list_of_strings)
    elif "divide" in command:
        list_of_strings = divide(int(command[1]), int(command[2]), list_of_strings)


