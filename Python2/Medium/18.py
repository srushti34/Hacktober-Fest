def filter_positive_numbers(lst):
 positive_numbers = []
 for num in lst:
 if num > 0:
 positive_numbers.append(num)
 elif num == 0:
 print("Zero is neither positive nor negative")
 return positive_numbers
 def main():
 numbers = [1, -2, 3, 0, -5, 4]
 filtered = filter_positive_numbers(numbers)
 print(f"Positive numbers: {filtered}")
 main()