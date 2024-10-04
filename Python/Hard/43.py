def calculate_mean(lst):
 total = sum(lst)
 return total / len(lst)
 except ZeroDivisionError:
    return 0
