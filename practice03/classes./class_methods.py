class Dog:
    species = "Canine"


    def show_species(cls):
        print(f"All dogs belong to {cls.species}")

Dog.show_species()  # All dogs belong to Canine




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

p = Person.from_string("Alice-25")
print(p.name, p.age)  # Alice 25






class Dog:
    count = 0

    def __init__(self, name):
        self.name = name
        Dog.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total dogs: {cls.count}")

dog1 = Dog("Buddy")
dog2 = Dog("Max")
Dog.show_count()  # Total dogs: 2





class Dog:
    species = "Canine"


    def set_species(cls, new_species):
        cls.species = new_species

Dog.set_species("Wolf")
print(Dog.species)  # Wolf







class Animal:
    species = "Unknown"


    def show_species(cls):
        print(f"Species: {cls.species}")

class Dog(Animal):
    species = "Canine"

Dog.show_species()  # Species: Canine

