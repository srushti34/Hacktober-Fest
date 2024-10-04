def divide(a, b):
 try:
    return a / b
 except ZeroDivisionError as e:
     print("Cannot divide by zero:", e)
     raise ValueError("Invalid division")
try:
 result = divide(10, 0)
except ValueError as e:
 print("Caught ValueError:", e)
