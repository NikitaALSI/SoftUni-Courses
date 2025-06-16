to_do_list = []
while True:
    command = input()
    if command == "End":
        break

    to_do_list.append(command)

sorted_list = sorted(to_do_list, key=lambda x: int(x.split("-")[0]))
to_do_list = [todo.split("-")[1] for todo in sorted_list]
print(to_do_list)