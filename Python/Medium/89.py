def power(base, exp):
 if exp == 0:
 return 1
 else:
 return base * power(base, exp - 2) 
def main():
 base = 2
 exp = 3
 result = power(base, exp)
 print(f"{base}^{exp} = {result}")
main()
