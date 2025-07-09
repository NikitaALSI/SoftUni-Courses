number_of_commands = int(input())
parked_cars = {}


def register(name, plate):
    if name in parked_cars.keys():
        print(f"ERROR: already registered with plate number {parked_cars[name]}")
    else:
        parked_cars[name] = plate
        print(f"{name} registered {plate} successfully")


def unregister(name):
    if name not in parked_cars.keys():
        print(f"ERROR: user {name} not found")
    else:
        del parked_cars[name]
        print(f"{name} unregistered successfully")


def print_parked_cars(parked: dict):
    for name, car in parked_cars.items():
        print(f"{name} => {car}")


for _ in range(number_of_commands):
    cmd = input()
    if cmd.startswith("register"):
        username, car_plate = cmd.split()[1:]
        register(username, car_plate)
    elif cmd.startswith("unregister"):
        username = cmd.split()[-1]
        unregister(username)

print_parked_cars(parked_cars)
