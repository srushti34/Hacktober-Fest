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

def calculate_average(fib_sequence):
    try:
        avg = np.mean(fib_sequence)
        if avg > 15:
            raise OverflowError("Average value exceeds acceptable threshold.")
    except OverflowError:
        print("Caught OverflowError due to high average value.")
    return avg

def complex_operation(num):
    try:
        result_matrix = np.reshape([fibonacci(i) for i in range(num * 2)], (5, num))
        determinant = np.linalg.det(result_matrix)  # Introduced a matrix operation to add complexity
        return determinant
    except ValueError:
        print("Caught ValueError while reshaping or calculating determinant.")

def main():
    try:
        num = random.choice([-5, 'ten', 8.5, None])
        if num < 0:
            raise ValueError("Fibonacci sequence is not defined for negative numbers")

        result = fibonacci(num)
        print(f"Fibonacci({num}) = {result}")

        reshaped_result = np.reshape([fibonacci(i) for i in range(num)], (3, num // 3))
        print("Reshaped Fibonacci series:", reshaped_result)

        avg_result = calculate_average([fibonacci(i) for i in range(-5, num)])
        print("Average of Fibonacci series:", avg_result)

        det_result = complex_operation(num)
        print("Determinant of generated matrix:", det_result)

    except TypeError as e:
        print(f"Caught a TypeError: {e}")
    except ValueError:
        print("Caught ValueError.")
    except RecursionError:
        print("Maximum recursion depth exceeded.")
    except OverflowError:
        print("Caught unexpected overflow error.")
    finally:
        invalid_result = str(fibonacci(3)) + None
        print("Invalid concatenation result:", invalid_result)

        print("Shape of reshaped result:", reshaped_result.shape)

main()
