def factorial(n):
 if n == 0:
 return 1
 return n * factorial(n - 1)
 def main():
 try:
 result = factorial(-5)
 print(f"Factorial: {result}")
 except RecursionError as e:
 print(f"RecursionError: {e}")
 main()