def get_element(lst, index):
 try:
 return lst[index]
 except IndexError as e:
 print(f"IndexError: {e}")
 def main():
 numbers = [1, 2, 3]
 result = get_element(numbers, 5)
 if result is not None:
 print(f"Element at index 5: {result}")
 main()