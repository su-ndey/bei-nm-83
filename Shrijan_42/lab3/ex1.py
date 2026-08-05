import numpy as np

# Get dimensions for the coefficient matrix A
rows = int(input("Enter the number of rows in the coefficient matrix (A): "))
cols = int(input("Enter the number of columns in the coefficient matrix (A): "))
print("Enter the matrix entries row by row, with entries separated by spaces:")

matrix_entries = []
for i in range(rows):
    row_entries = input(f"Row {i + 1}: ").split()
    matrix_entries.append([float(entry) for entry in row_entries])

A = np.array(matrix_entries, dtype=np.float64)

# Get dimensions for the constants matrix B (usually should be rows x 1)
b_rows = rows
b_cols = 1
print("Enter the constants entries row by row, with entries separated by spaces:")

constants_entries = []
for i in range(b_rows):
    row_entries = input(f"Row {i + 1}: ").split()
    constants_entries.append([float(entry) for entry in row_entries])

B = np.array(constants_entries, dtype=np.float64)

pivot=0
for i in range(rows):
    for j in range(i+1,rows):
        if A[i,i] < A[j,i]:
            pivot=j
            break
    if pivot!=i:
        A[[i, pivot], :] = A[[pivot, i], :]
        B[[i, pivot]] = B[[pivot, i]]
   
    for j in range(i+1,rows):
        factor = A[j,i] / A[i,i]
        for k in range(i,cols):
            A[j,k] -= factor * A[i,k]
        B[j] -= factor * B[i]

x = np.zeros(rows)
for i in range(rows - 1, -1, -1):
    b_i = B[i] if np.isscalar(B[i]) or B[i].shape == () else B[i][0]
    x[i] = b_i
    for j in range(i + 1, cols):
        x[i] -= A[i, j] * x[j]
    x[i] /= A[i, i]
print("The solution is: ", x.round().astype(int))