def safe_divide(a, b):
 if b == 0:
 return "Cannot divide by zero"
 return a / b
 def main():
 try:
 print(safe_divide(10, 0))
 print(safe_divide(0, 0))
 except ZeroDivisionError as e:
 print(f"ZeroDivisionError: {e}")
 main()