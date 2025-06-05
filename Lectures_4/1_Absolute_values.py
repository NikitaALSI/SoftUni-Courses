def absolute_string_to_list(values: str):
    lst = values.split(" ")
    return list(map(abs, map(float, lst)))


print(absolute_string_to_list(input()))