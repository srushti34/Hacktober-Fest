 def divide(a, b):
 try:
 return a / b
 except:
 print("An error occurred")
 return None
 def main():
 result = divide(10, 0)
 if result is not None:
 print(f"Result: {result}")
 main()