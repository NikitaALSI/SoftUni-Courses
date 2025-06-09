def smallest(some_list) -> list:
    """
    Give a list the function returns the smallest entity in the list

    :param some_list:
    :return: list
    """
    return min(some_list)


first = int(input())
second = int(input())
third = int(input())
my_list = [first, second, third]
print(smallest(my_list))