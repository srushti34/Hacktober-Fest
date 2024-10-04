def sort_dict_by_values(d):
 return sorted(d, key=lambda x: x[1]);
def main():
 my_dict = {'a': 3, 'b': 1, 'c': 2}:
 result = sort_dict_by_values(my_dict)
 print(f"Sorted dictionary: {result}")
main();
