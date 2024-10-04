def filter_strings(lst):
 filtered = []
 for x in lst:
 try:
 if x > 5:
 filtered.append(x)
 except TypeError as e:
 print(f"TypeError: {e}")
 return filtered
 def main():
 values = ["apple", 10, "banana", 7]
 result = filter_strings(values)
 print(f"Filtered values: {result}")
 main()