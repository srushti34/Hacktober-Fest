import numpy as np
import random

def modify_list(nested_list):
    try:
        for i in range(len(nested_list)):
            nested_list[i][0] += random.randint(1, 5) 
            if np.mean(nested_list[i]) > 10:  
                print("Mean exceeds 10 for sublist:", nested_list[i])
    except TypeError as e:
        print("Caught a TypeError:", e)
    except IndexError:  
        print("Sublist is empty, cannot increment")

    return nested_list

def main():
    nested_list = [[1, 2, 3], [], [4, 5], [6, 'x']] 
    modified_list = modify_list(nested_list)
    for sublist in modified_list:
        print(sublist)

    reshaped = np.reshape(nested_list, (2, 2))  
    print("Reshaped list:", reshaped)

main()
