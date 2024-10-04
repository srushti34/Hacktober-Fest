def append_to_list(item, lst=[]):
 lst.append(item)
 return lst
 def main():
 list1 = append_to_list(1)
 print(f"List after first append: {list1}")
 list2 = append_to_list(2)
 print(f"List after second append: {list2}")
 main()