activation_key = input()

while (instructions := input()) != "Generate":
    if instructions.startswith("Contains"):
        substring = instructions.split(">>>")[-1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif instructions.startswith("Flip"):
        case, start, stop = instructions.split(">>>")[1:]
        activation_key = (activation_key[:int(start)] +
                          (activation_key[int(start):int(stop)].upper() if case == "Upper"
                           else activation_key[int(start):int(stop)].lower()) +
                          activation_key[int(stop):])
        print(activation_key)
    elif instructions.startswith("Slice"):
        start, stop = instructions.split(">>>")[1:]
        activation_key = activation_key[:int(start)] + activation_key[int(stop):]
        print(activation_key)
print(f"Your activation key is: {activation_key}")
