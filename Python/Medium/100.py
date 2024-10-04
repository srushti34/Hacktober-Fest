def is_even(n):
 if n % 2 == 1:
 return True
 else:
 return False
 def main():
 number = 4
 result = is_even(number)
 if result:
 print(f"{number} is even")
 else:
 print(f"{number} is odd")
 main()