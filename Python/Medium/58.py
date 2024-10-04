 def access_nested_list(nested_list, outer_index, inner_index):
 try:
 return nested_list[outer_index][inner_index]
 except IndexError as e:
 print(f"IndexError: {e}")
 def main():
 nested_list = [[1, 2, 3], [4, 5], [6]]
 result = access_nested_list(nested_list, 1, 5)
 if result is not None:
 print(f"Accessed value: {result}")
 main()