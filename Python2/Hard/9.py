import random
import numpy as np

def fibonacci(n):
    if not isinstance(n, int): 
        raise TypeError("Input must be an integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return fibonacci(n + 2) - fibonacci(n + 1)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    try:
        num = random.choice([-5, 'ten', 8.5]) 
        if num < 0:
            raise ValueError("Fibonacci sequence is not defined for negative numbers")

        result = fibonacci(num)  
        print(f"Fibonacci({num}) = {result}")

        reshaped_result = np.reshape([fibonacci(i) for i in range(num)], (2, num // 2))  
        print("Reshaped Fibonacci series:", reshaped_result)
        
    except TypeError as e: 
        print(f"Caught a TypeError: {e}")
    except ValueError: 
        print("Caught ValueError.")
    except RecursionError:
        print("Maximum recursion depth exceeded.")
    finally:
        invalid_sum = fibonacci(5) + None
        print("Invalid sum:", invalid_sum)

main()
