# people = input().split(" ")
# k = int(input())
# killed = []
# nth = 0
#
# while people:
#     nth_killed = []
#     indexes = []
#     for index in range(len(people)):
#         nth += 1
#         if nth == k:
#             nth_killed.append(people[index])
#             indexes.append(index)
#             nth = 0
#     adds = 0
#     for index in indexes:
#         people.pop(index - adds)
#         adds += 1
#
#     killed.extend(nth_killed)
#
# string = ",".join(killed)
# print(f"[{string}]")

initial_circle = input().split()
skip_count = int(input())

# this is to make sure k-1 people are skipped and the k person is executed
# when k is positive
if skip_count > 0:
    skip_count -= 1

# this is to rule out a case when k is negative
# in this case we just reverse the list, make k positive and return to the main case
elif skip_count < 0:
    initial_circle = initial_circle[::-1]
    skip_count *= -1

execution_list = []
list_length = len(initial_circle)
idx = skip_count

while initial_circle:

    # this is to make sure k is less than the list length at all times
    while idx >= list_length and initial_circle:
        idx -= list_length

    execution_list.append(initial_circle[idx])
    initial_circle.remove(initial_circle[idx])
    list_length = len(initial_circle)

    # this if statement is to manage the case when the elements left in the list are fewer than k
    # and another iteration through the list is needed
    if idx + skip_count > list_length:
        elements_left = list_length - idx
        idx = skip_count - elements_left

    else:
        idx += skip_count

formatted_execution_list = ",".join(execution_list)
print(f"[{formatted_execution_list}]")