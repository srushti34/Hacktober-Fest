import numpy as np

def add_arrays(arr1, arr2):
    try:
        return arr1 * arr2  # Error 1: Changed from addition to multiplication (logic error)
    except ValueEror as e:  # Error 2: Typo in 'ValueError' (syntax error)
        print(f"ValueEror: {e}")

def main():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([[1, 2], [3, 4]])  # Error 3: Incorrect shape (logic error, incompatible for broadcasting)

    result = add_arrays(arr1, arr2)
    print(f"Result: {result}")

main()
