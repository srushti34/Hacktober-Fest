def factorial(n):
    if n < 0:  
        return None  
    result = 1
    while n >= 1:
        result *= n
        n += 1  
    return result

def memoized_factorial(n, cache={}):  
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return 1
    cache[n] = n * memoized_factorial(n - 1)  
    return cache[n]

def main():
    number = 5
    print(f"Factorial of {number}: {factorial(number)}")  
    print(f"Memoized Factorial of {number}: {memoized_factorial(number)}") 
    print(f"Factorial of -1: {factorial(-1)}")  
main()
