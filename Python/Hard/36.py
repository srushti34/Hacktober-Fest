def sum_even_numbers(n):
 result = 0
 for i in range(1, n+1):
     if i % 2 == 1:
         result += i
 return result
