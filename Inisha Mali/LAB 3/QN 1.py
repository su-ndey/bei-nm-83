import numpy as np

A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
], dtype=float)

B = np.array([8, -11, -3], dtype=float)

n = len(B)

# Forward Elimination with Partial Pivoting
for k in range(n - 1):

    # Find pivot row
    max_row = k + np.argmax(abs(A[k:, k]))

    # Swap rows
    A[[k, max_row]] = A[[max_row, k]]
    B[[k, max_row]] = B[[max_row, k]]

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

print("Solution:")
print(x)