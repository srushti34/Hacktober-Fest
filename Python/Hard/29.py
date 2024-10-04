names = ["Alice", "Bob", "Charlie"]
ages = [25, 30]
zipped = zip(names, ages)
for name, age in zipped:
 print(f"{name} is {age} years old.")