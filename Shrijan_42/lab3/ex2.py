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

# Comment out partial pivot
# pivot=0
# for i in range(rows):
#     for j in range(i+1,rows):
#         if A[i,i] < A[j,i]:
#             pivot=j
#             break
#     if pivot!=i:
#         A[[i, pivot], :] = A[[pivot, i], :]
#         B[[i, pivot]] = B[[pivot, i]]
   
#     for j in range(i+1,rows):
#         factor = A[j,i] / A[i,i]
#         for k in range(i,cols):
#             A[j,k] -= factor * A[i,k]
#         B[j] -= factor * B[i]

# Use full pivot
col_index = np.arange(cols)
for i in range(rows):
    # Find the max element for full pivoting in submatrix A[i:rows, i:cols]
    sub_matrix = np.abs(A[i:rows, i:cols])
    max_idx = np.unravel_index(np.argmax(sub_matrix), sub_matrix.shape)
    pivot_row, pivot_col = max_idx[0] + i, max_idx[1] + i

    # Swap rows in A and B
    if pivot_row != i:
        A[[i, pivot_row], :] = A[[pivot_row, i], :]
        B[[i, pivot_row]] = B[[pivot_row, i]]

    # Swap columns in A and keep track of column swaps
    if pivot_col != i:
        A[:, [i, pivot_col]] = A[:, [pivot_col, i]]
        col_index[[i, pivot_col]] = col_index[[pivot_col, i]]

    # Elimination process
    for j in range(i+1, rows):
        if A[i, i] == 0:
            continue  # skip to avoid ZeroDivisionError in degenerate cases
        factor = A[j, i] / A[i, i]
        A[j, i:cols] -= factor * A[i, i:cols]
        B[j] -= factor * B[i]

x = np.zeros(rows)
# Perform back substitution to solve for x in the upper triangular system
for i in range(rows - 1, -1, -1):
    # Start with the right-hand side value for variable i
    b_i = B[i] if np.isscalar(B[i]) or B[i].shape == () else B[i][0]
    x[i] = b_i
    # Subtract the known values of x for columns j > i (since A is upper triangular here)
    for j in range(i + 1, cols):
        x[i] -= A[i, j] * x[j]
    # Divide by the diagonal coefficient to solve for x[i]
    x[i] /= A[i, i]

# Undo column swaps to get x in the correct order
actual_x = np.zeros_like(x)
for i in range(rows):
    actual_x[col_index[i]] = x[i]

# Output as integers to match the prompt's expected output
print("The solution is: ", actual_x.round().astype(int))