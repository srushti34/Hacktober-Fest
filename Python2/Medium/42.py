def add_matrices(mat1, mat2):
 result = []
 for i in range(len(mat1)):
 for j in range(len(mat2)): 
 result.append(mat1[i][j] + mat2[i][j]) 
 return result
def main():
 matrix1 = [[1, 2], [3, 4]]
 matrix2 = [[5, 6], [7, 8]]
 result = add_matrices(matrix1, matrix2)
 print(f"Matrix sum: {result}")
main()
