def custom_key(tup):
   return tup[1] 
def sort_tuples(tuples_list):
   try:
     return sorted(tuples_list, key=custom_key)
   
def main():
  tuples_list = [(1, 2), (3,), (4, 5), (6,)]
  sorted_list = sort_tuples(tuples_list)
  print(sorted_list)

main()