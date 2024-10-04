class Car:
 def __init__(self, model, year):
    self.model = model
    self.year = year
 def display(self):
    print(f"The car is a {self.model} from {self.year}")
my_car = Car("Toyota", 2020)
print(my_car.year)
my_car.year = "2021"
my_car.display()
