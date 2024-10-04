def find_max(lst):
 max_val = lst[0]
 for i in range(len(lst)):
 if lst[i] < max_val: 
 max_val = lst[i]
 return max_val
def main():
 numbers = [1, 4, 2, 8, 3]
 result = find_max(numbers)
 print(f"Max value: {result}")
main()