students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


nums = [-10, 3, -2, 7]
print(sorted(nums, key=lambda x: abs(x)))


words = ["apple", "kiwi", "banana"]
print(sorted(words, key=lambda x: len(x)))


pairs = [(1, 3), (4, 1), (2, 2)]
print(sorted(pairs, key=lambda x: x[1]))

