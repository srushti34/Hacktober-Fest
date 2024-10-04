 def find_number(lst, target):
 for num in lst:
 if num == target:
 print(f"Found {target}")
 break
 else:
 print(f"{target} not found in the list")
 def main():
 numbers = [1, 2, 3, 4, 5]
 find_number(numbers, 6)
 main()