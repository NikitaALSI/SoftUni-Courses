class Vehicle:
    def __init__(self, type: str, model: str, price: int):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if not self.owner and money >= self.price:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
        elif not self.owner:
            return "Sorry, not enough money"
        return "Car already sold"

    def sell(self):
        if self.owner:
            self.owner = None
        return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)

