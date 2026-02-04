class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()



class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        super().move()
        print("Car is moving fast")

c = Car()
c.move()



class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Alice", 10)
print(s.name, s.grade)



class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return 4 * 4

sq = Square()
print(sq.area())



class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

birds = [Bird(), Penguin()]

for b in birds:
    b.fly()
