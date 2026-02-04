class Dog:
    species = "Canine"  # class variable

dog1 = Dog()
dog2 = Dog()

print(dog1.species)  # Canine
print(dog2.species)  # Canine



class Dog:
    species = "Canine"

dog1 = Dog()
dog2 = Dog()

Dog.species = "Wolf"

print(dog1.species)  # Wolf
print(dog2.species)  # Wolf




class Dog:
    species = "Canine"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.name, dog1.species)  # Buddy Canine
print(dog2.name, dog2.species)  # Max Canine




class Dog:
    count = 0  # class variable

    def __init__(self, name):
        self.name = name
        Dog.count += 1

dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Rocky")

print(Dog.count)  # 3




class Dog:
    species = "Canine"

    def print_species(self):
        print(f"This dog is a {Dog.species}")

dog1 = Dog()
dog1.print_species()  # This dog is a Canine
