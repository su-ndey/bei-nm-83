import numpy as np

# System matrix definition
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
], dtype=float)

B = np.array([8, -11, -3], dtype=float)

n = len(B)

# Gauss-Jordan Elimination
for k in range(n):

    # Partial Pivoting
    if abs(A[k, k]) < 1e-12:
        for i in range(k + 1, n):
            if abs(A[i, k]) > abs(A[k, k]):
                A[[k, i]] = A[[i, k]]
                B[[k, i]] = B[[i, k]]
                break

    # Make pivot element equal to 1
    pivot = A[k, k]
    A[k] = A[k] / pivot
    B[k] = B[k] / pivot

    # Make all other elements in the pivot column zero
    for i in range(n):
        if i != k:
            factor = A[i, k]
            A[i] = A[i] - factor * A[k]
            B[i] = B[i] - factor * B[k]

# Display results
print("Reduced Row Echelon Form (RREF):")
print(A)

print("\nGauss-Jordan Solution Vector:")
print(B)