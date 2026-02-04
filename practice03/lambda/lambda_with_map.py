numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)



numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


nums = [1, 2, 3, 4]
print(list(map(lambda x: x ** 2, nums)))


words = ["apple", "hi", "python"]
print(list(map(lambda x: len(x), words)))



nums = [5, 10, 15]
print(list(map(lambda x: x + 10, nums)))



words = ["cat", "dog"]
print(list(map(lambda x: x.upper(), words)))
