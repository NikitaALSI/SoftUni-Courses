number_of_cars = int(input())
cars = {}
for _ in range(number_of_cars):
    car, milage, fuel = input().split("|")
    cars[car] = {"mileage": int(milage), "fuel": int(fuel)}

while (cmd := input()) != "Stop":
    if cmd.startswith("Drive"):
        car, distance, fuel = cmd.split(" : ")[1:]
        if cars[car]["fuel"] - int(fuel) <= 0:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -= int(fuel)
            cars[car]["mileage"] += int(distance)
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100000:
                del cars[car]
                print(f"Time to sell the {car}!")
    elif cmd.startswith("Refuel"):
        car, fuel = cmd.split(" : ")[1:]
        charge = min(75 - cars[car]["fuel"], int(fuel))
        cars[car]["fuel"] += charge
        print(f"{car} refueled with {charge} liters")
    elif cmd.startswith("Revert"):
        car, kilometers = cmd.split(" : ")[1:]
        cars[car]["mileage"] -= int(kilometers)
        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
            continue
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car in cars:
    mileage = cars[car]["mileage"]
    fuel = cars[car]["fuel"]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")



