import numpy as np

rows = int(input("Enter the number of rows in the coefficient matrix (A): "))
cols = int(input("Enter the number of columns in the coefficient matrix (A): "))
print("Enter the matrix entries row by row, with entries separated by spaces:")

matrix_entries = []
for i in range(rows):
    row_entries = input(f"Row {i + 1}: ").split()
    matrix_entries.append([float(entry) for entry in row_entries])

A = np.array(matrix_entries, dtype=np.float64)
matrix_entries = []
for i in range(rows):
    row_entries = input(f"Row {i + 1} of B: ").split()
    matrix_entries.append([float(entry) for entry in row_entries])
B = np.array(matrix_entries, dtype=np.float64).reshape((rows, 1))
n=len(B)

for k in range(n):
    for i in range(k+1,n):
        if abs(A[i][k]) > abs(A[k][k]):
            A[[k, i]] = A[[i, k]]
            B[[k, i]] = B[[i, k]]
            break
    pivot=A[k][k]
    A[k]=A[k]/pivot
    B[k]=B[k]/pivot
    for i in range(k+1,n):
        factor=A[i][k]
        A[i]=A[i]-factor*A[k]
        B[i]=B[i]-factor*B[k]

print("The solution is: \n", B.round().astype(int))
