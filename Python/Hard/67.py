import numpy 

def replace_odd_numbers(arr):
    try:
        arr[arr % 2 == 1] = "Odd" 
    except TypeError as e:
        print(f"TypError: {e}") 

    return arr

def main():
    arr = np.array([1, 2, 3, 4, "5.5"]) 
    modified_arr = replace_odd_numbers(arr)
    print(f"Modified Array: {modified_arr}")

main()
