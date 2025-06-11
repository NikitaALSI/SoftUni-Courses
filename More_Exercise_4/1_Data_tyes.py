def operate(operation, some_string):
    actions = {}
    if operation == "int":
        actions["int"] = int(some_string) * 2
    elif operation == "real":
        actions["real"] = f"{float(some_string) * 1.5:.2f}"
    else:
        actions["string"] = f"${some_string}$"
    return actions[operation]


do = input()
string = input()

print(operate(do, string))