class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    
    
    
    
    
    
  class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Alice", 10)
print(s.name, s.grade)







class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

class C(B):
    def show(self):
        super().show()
        print("Class C")

c = C()
c.show()





class Logger:
    def log(self):
        print("Logging started")

class FileLogger(Logger):
    def log(self):
        super().log()
        print("Logging to file")

f = FileLogger()
f.log()



class Shape:
    def area(self):
        print("Calculating area")

class Rectangle(Shape):
    def area(self):
        super().area()
        print("Rectangle area = width * height")

r = Rectangle()
r.area()
