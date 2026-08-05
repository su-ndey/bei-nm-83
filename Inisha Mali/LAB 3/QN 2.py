import numpy as np

A = np.array([
    [0, 2, 1],
    [1, -2, -3],
    [2, 3, 1]
], dtype=float)

B = np.array([8, -11, -3], dtype=float)

n = len(B)

# Track column swaps
col_index = np.arange(n)

# Forward Elimination
for k in range(n - 1):

    # Find maximum element in remaining submatrix
    sub = abs(A[k:, k:])
    row, col = np.unravel_index(np.argmax(sub), sub.shape)

    row += k
    col += k

    # Swap rows
    A[[k, row]] = A[[row, k]]
    B[[k, row]] = B[[row, k]]

    # Swap columns
    A[:, [k, col]] = A[:, [col, k]]
    col_index[[k, col]] = col_index[[col, k]]

    # Elimination
    for i in range(k + 1, n):
        factor = A[i][k] / A[k][k]

        for j in range(k, n):
            A[i][j] -= factor * A[k][j]

        B[i] -= factor * B[k]

# Back Substitution
x = np.zeros(n)

for i in range(n - 1, -1, -1):
    sum_ax = 0

    for j in range(i + 1, n):
        sum_ax += A[i][j] * x[j]

    x[i] = (B[i] - sum_ax) / A[i][i]

# Rearrange variables
final_x = np.zeros(n)

for i in range(n):
    final_x[col_index[i]] = x[i]

print("Solution:")
print(final_x)