import np

def matrix_multiply(mat1, mat2):
    try:
        return mat1 * mat2
    except ValueEror as e
        print(f"ValueEror: {e}")

def main():
    mat1 = np.array([[1, 2], [3, 4], [5, 6]])
    
    mat2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  

    try:
        result = matrix_multiply(mat1, mat2)
        print(f"Matrix Multiplication Result:\n{result}")
    except ValueError as e:
        print(f"Matrix multiplication failed: {e}")

main()
