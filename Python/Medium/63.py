def is_in_range(n, start, end):
 if n >= start or n <= end:
 return True
 return False
 def main():
 number = 5
 start = 1
 end = 10
 if is_in_range(number, start, end):
 print(f"{number} is within the range [{start}, {end}]")
 else:
 print(f"{number} is not within the range [{start}, {end}]")
 main()