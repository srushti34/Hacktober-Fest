class Employee:
 def __init__(self, name, salary):
   self.name = name
   self.salary = salary
 def give_raise(self, amount):
   self.salary += amount
employee = Employee('John', 50000)
employee.give_raise(5000)
print(employee.salary())