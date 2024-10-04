def factorial(n):
 if n < 0:
 return "Factorial not defined for negative numbers"
 result = 1
 for i in range(n):
 result *= i
 return result
 def main():
 try:
 value = 5
 result = factorial(value)
 print(f"Factorial of {value} is {result}")
 except Exception as e:
 print(f"Error: {e}")
 main()