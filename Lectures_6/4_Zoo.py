class Zoo:

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
        self.animals = 0

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.animals += 1

    def get_info(self, species):
        if species == "mammal":
            print(f"{species.capitalize()}s in {self.name}: {', '.join(self.mammals)}" )
        elif species == "fish":
            print(f"{species.capitalize()}es in {self.name}: {', '.join(self.fishes)}")
        elif species == "bird":
            print(f"{species.capitalize()}s in {self.name}: {', '.join(self.birds)}")
        print(f"Total animals: {self.animals}")


zoo = Zoo(input())
for _ in range(int(input())):
    some_species, some_name = input().split()
    zoo.add_animals(some_species, some_name)
zoo.get_info(input())

