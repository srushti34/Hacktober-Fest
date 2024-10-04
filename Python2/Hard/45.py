import numpy as np

def add_arrays(arr1, arr2):
    try:
        return arr1 + arr2 
    except ValueError as e:
        print(f"ValueError: {e}")

def main():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([[1], [2]])  
    result = add_arrays(arr1, arr2)
    print(f"Result: {result}")

main()
