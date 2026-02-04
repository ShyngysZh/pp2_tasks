class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()


class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Alice", 10)
print(s.name, s.grade)


class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def honk(self):
        print("Beep beep")

c = Car()
c.move()
c.honk()



class Shape:
    pass

class Circle(Shape):
    pass

c = Circle()

print(isinstance(c, Circle))  # True
print(isinstance(c, Shape))   # True
