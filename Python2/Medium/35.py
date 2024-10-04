def sum_of_elements(lst):
 total = 0
 for i in range(len(lst)):
 total += lst[i + 1] 
 return total
def main():
 numbers = [1, 2, 3, 4]
 result = sum_of_elements(numbers)
 print(f"Sum: {result}")
main()
