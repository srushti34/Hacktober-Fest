 def concatenate_strings(lst):
 result = ""
 for item in lst:
 result += item
 return result
 def main():
 items = ["Hello", " ", 123, "World!"]
 try:
 result = concatenate_strings(items)
 print(result)
 except TypeError as e:
 print(f"TypeError: {e}")
 main()