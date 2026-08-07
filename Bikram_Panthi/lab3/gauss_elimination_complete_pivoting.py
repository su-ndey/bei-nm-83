# Lab 3 - Gaussian Elimination with Complete Pivoting
# Pure Python - matrices are nested lists, no external libraries needed.
#
# Both rows AND columns are swapped, so I track the column swaps in col_index and
# put the variables back into their original order at the end (step 8 of the
# algorithm given in the lab sheet).
#
# System:       2y +  z =   8
#          x - 2y - 3z = -11
#         2x + 3y +  z =  -3

A = [
    [0, 2, 1],
    [1, -2, -3],
    [2, 3, 1]
]

B = [8, -11, -3]

A = [[float(value) for value in row] for row in A]
B = [float(value) for value in B]

n = len(B)

# Track column swaps so the variables can be put back in order later
col_index = list(range(n))

# Forward Elimination
for k in range(n - 1):

    # Find the largest absolute element in the remaining submatrix A[k:, k:]
    max_row, max_col = k, k
    for i in range(k, n):
        for j in range(k, n):
            if abs(A[i][j]) > abs(A[max_row][max_col]):
                max_row, max_col = i, j

    # Swap rows
    A[k], A[max_row] = A[max_row], A[k]
    B[k], B[max_row] = B[max_row], B[k]

    # Swap columns
    for row in A:
        row[k], row[max_col] = row[max_col], row[k]
    col_index[k], col_index[max_col] = col_index[max_col], col_index[k]

    # Elimination
    for i in range(k + 1, n):

        factor = A[i][k] / A[k][k]

        for j in range(k, n):
            A[i][j] -= factor * A[k][j]

        B[i] -= factor * B[k]

# Back Substitution
x = [0.0] * n

for i in range(n - 1, -1, -1):

    sum_ax = 0.0

    for j in range(i + 1, n):
        sum_ax += A[i][j] * x[j]

    x[i] = (B[i] - sum_ax) / A[i][i]

# Rearrange the variables according to the column swaps
solution = [0.0] * n
for i in range(n):
    solution[col_index[i]] = x[i]

print("Solution:")
for i in range(n):
    print(f"x{i + 1} = {solution[i]:.6f}")
