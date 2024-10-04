def dict_depth(d, level=1):
  if not isinstance(d, dict):
    return level
  max_depth = level
  for key in d:
     max_depth = max(max_depth, dict_depth(d[key], level + 1))
  return max_depth
def main():
  nested_dict = {"a": {"b": {"c": {}}}, "d": "e"}
  try:
     depth = dict_depth(nested_dict)
     print(f"Depth of dictionary: {depth}")
  except RecursionError as e:
     print(f"RecursionError: {e}")
main()