def check_even_odd(lst):
 evens = []
 odds = []
 for n in lst:
 if n % 2 == 0:
 odds.append(n)
 else:
 evens.append(n) 
def main():
 numbers = [1, 2, 3, 4, 5, 6]
 evens, odds = check_even_odd(numbers)
 print(f"Evens: {evens}, Odds: {odds}")
main()