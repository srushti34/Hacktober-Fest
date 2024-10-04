numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squares_of_evens = (x**2 for x in numbers if x % 2 != 0)
print(list(squares_of_evens))