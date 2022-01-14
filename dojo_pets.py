from msilib.schema import Class


class Ninja:
    def __init__(self,first_name, last_name, treats, pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self,pet):
        print("you are walking your pet")
        Pet.play(pet)
        return self
    def feed(self,pet):
        print(f"you fed {pet.name}")
        Pet.eat(pet)
        return self
    def bathe(self,pet):
        print(f"you bathed {pet.name}")
        Pet.noise(pet)
        return self


class Pet():
    def __init__(self,name,type,tricks,health,energy):
        # super().__init__(pet)
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        print(f"{self.name} slept!")

    def eat(self):
        self.energy += 5
        self.health += 20
        print(f"{self.name} was fed, energy is at {self.energy} and health is at {self.health}")
        return self

    def play(self):
        self.health += 10
        print(f"{self.name} enjoyed that! Its health is now {self.health}")
        return self

    def noise(self):
        print(f"{self.name} made a noise")

Scooby_doo = Pet("Scooby doo","Dog","Talk",100,100)
shaggy = Ninja("Shaggy","Rogers","scooby snacks","sandwhich", Scooby_doo)

shaggy.walk(shaggy.pet)
shaggy.feed(shaggy.pet)
shaggy.bathe(shaggy.pet)
# print(Scooby_doo.name)
print(Scooby_doo.health)
print(Scooby_doo.energy)