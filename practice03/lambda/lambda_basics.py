x = lambda a : a + 10
print(x(5))


x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


add = lambda a, b: a + b
print(add(3, 5))
# same as 
def add(a, b):
    return a + b


is_even = lambda x: x % 2 == 0
print(is_even(4))
# same as
def is_even(x):
    return x % 2 == 0




  
  def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
