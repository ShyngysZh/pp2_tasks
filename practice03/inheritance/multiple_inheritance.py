class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greet()  # Output: Hello from A





class A:
    def show(self):
        print("A class method")

class B:
    def show(self):
        print("B class method")

class C(A, B):
    def show(self):
        print("C class method")

c = C()
c.show()  # Output: C class method




class A:
    def display(self):
        print("A display")

class B:
    def display(self):
        print("B display")

class C(A, B):
    def display(self):
        super().display()
        print("C display")

c = C()
c.display()






class A:
    def __init__(self):
        print("Constructor A")

class B:
    def __init__(self):
        print("Constructor B")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("Constructor C")

c = C()





class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Painting")

class Child(Father, Mother):
    def skills(self):
        super().skills()  # calls Father.skills()
        print("Gaming, Sports")

c = Child()
c.skills()
