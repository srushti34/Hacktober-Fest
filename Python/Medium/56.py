def sort_list(lst):
 try:
 lst.sort()
return lst
 except TypeError as e:
 print(f"TypeError: {e}")
 def main():
 items = [5, "banana", 3, "apple"]
 sorted_items = sort_list(items)
 if sorted_items:
 print(f"Sorted items: {sorted_items}")
 main()