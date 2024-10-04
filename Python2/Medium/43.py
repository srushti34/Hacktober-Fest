def merge_sorted_lists(lst1, lst2):
 merged = []
 i = j = 0
 while i < len(lst1) and j < len(lst2):
  if lst1[i] > lst2[j]: 
 merged.append(lst1[i])
 i += 1
 else:
 merged.append(lst2[j])
 j += 1
 merged += lst1[i:]
 merged += lst2[j:]
 return merged
def main():
 list1 = [1, 3, 5]
 list2 = [2, 4, 6]
 result = merge_sorted_lists(list1, list2)
 print(f"Merged list: {result}")
main()
