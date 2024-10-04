def fibonacci(n):
 if n == 0:
 return 0
 elif n == 1:
 return 1
 else:
 return fibonacci(n - 1) + fibonacci(n - 2)
def main():
try:
Intermediate Level Code Snippets 18
 result = fibonacci(-3)
 print(f"Fibonacci: {result}")
 except RecursionError as e:
 print(f"RecursionError: {e}")
main()
