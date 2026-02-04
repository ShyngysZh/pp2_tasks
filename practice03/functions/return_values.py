def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))



def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)



def get_coordinates():
    return (5, 10)

x, y = get_coordinates()
print(f"x: {x}, y: {y}")


def is_positive(num):
    return num > 0

print(is_positive(10))
print(is_positive(-5))




def get_even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

print(get_even_numbers([1, 2, 3, 4, 5, 6]))

