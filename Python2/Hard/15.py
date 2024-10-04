def matrix_multiply(matrix1, matrix2):
   if len(matrix1[0]) != len(matrix2):
     raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
   result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
   for i in range(len(matrix1)):
     for j in range(len(matrix2[0])):
         for k in range(len(matrix1[0])):
             result[i][j] += matrix1[i][k] * matrix2[k][j] 
   return result

def main():
   matrix1 = [[1, 2, 3], [4, 5, 6]]
   matrix2 = [[7, 8], [9, 10]] 
   try:
     result = matrix_multiply(matrix1, matrix2)
     for row in result:
         print(row)
   except ValueError as e:
     print(f"ValueError: {e}")
main()