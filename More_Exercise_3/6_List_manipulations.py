the_list = list(map(int, input().split(" ")))

while True:
    command = input().split(" ")
    if command == ["end"]:
        print(the_list)
        break
    if "exchange" in command:
        if int(command[1]) in range(0, len(the_list)):
            first_part = the_list[:int(command[1]) + 1]
            second_part = the_list[int(command[1]) + 1:]
            second_part.extend(first_part)
            the_list = second_part
        else:
            print("Invalid index")

    elif "max" in command:
        if command[1] == "odd":
            if list(filter(lambda x: x % 2 != 0, the_list)):
                max_odd = max(filter(lambda x: x % 2 != 0, the_list))
                print(len(the_list) - the_list[::-1].index(max_odd) - 1)
            else:
                print("No matches")
        elif command[1] == "even":
            if list(filter(lambda x: x % 2 == 0, the_list)):
                max_even = max(filter(lambda x: x % 2 == 0, the_list))
                print(len(the_list) - the_list[::-1].index(max_even) - 1)
            else:
                print("No matches")
    elif "min" in command:
        if command[1] == "odd":
            if list(filter(lambda x: x % 2 != 0, the_list)):
                max_odd = min(filter(lambda x: x % 2 != 0, the_list))
                print(len(the_list) - the_list[::-1].index(max_odd) - 1)
            else:
                print("No matches")
        elif command[1] == "even":
            if list(filter(lambda x: x % 2 == 0, the_list)):
                max_even = min(filter(lambda x: x % 2 == 0, the_list))
                print(len(the_list) - the_list[::-1].index(max_even) - 1)
            else:
                print("No matches")

    elif "first" in command:
        if int(command[1]) <= len(the_list):
            if command[2] == "odd":
                odd_list = list(filter(lambda x: x % 2 != 0, the_list))
                if int(command[1]) > len(odd_list):
                    print(odd_list)
                else:
                    print(odd_list[:int(command[1])])
            elif command[2] == "even":
                even_list = list(filter(lambda x: x % 2 == 0, the_list))
                if int(command[1]) > len(even_list):
                    print(even_list)
                else:
                    print(even_list[:int(command[1])])
        else:
            print("Invalid count")
    elif "last" in command:
        if int(command[1]) <= len(the_list):
            if command[2] == "odd":
                odd_list = list(filter(lambda x: x % 2 != 0, the_list))
                if int(command[1]) > len(odd_list):
                    print(odd_list)
                else:
                    print(odd_list[len(odd_list) - int(command[1]):])
            elif command[2] == "even":
                even_list = list(filter(lambda x: x % 2 == 0, the_list))
                if int(command[1]) > len(even_list):
                    print(even_list)
                else:
                    print(even_list[len(even_list) - int(command[1]):])
        else:
            print("Invalid count")
