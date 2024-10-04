def get_value(d, key):
 try:
 return d[key]
 except KeyError as e:
 print(f"KeyError: {e}")
 return None
def main():
 my_dict = {"a": 1, "b": 2}
 value = get_value(my_dict, "c")
 if value is not None:
 print(f"Value for key 'c': {value}")
main()
