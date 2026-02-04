nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, nums)))



nums = [5, 12, 8, 20]
print(list(filter(lambda x: x > 10, nums)))


words = ["hi", "hello", "cat", "python"]
print(list(filter(lambda x: len(x) > 3, words)))


nums = [-3, 5, -1, 7]
print(list(filter(lambda x: x > 0, nums)))


nums = [3, 4, 6, 7, 9]
print(list(filter(lambda x: x % 3 == 0, nums)))
