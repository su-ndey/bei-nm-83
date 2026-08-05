import numpy as np

A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
], dtype=float)

B = np.array([8, -11, -3], dtype=float)
n = len(B)

for k in range(n):
    if abs(A[k, k]) < 1e-12:
        for i in range(k + 1, n):
            if abs(A[i, k]) > abs(A[k, k]):
                A[[k, i]] = A[[i, k]]
                B[[k, i]] = B[[i, k]]
                break

    pivot = A[k, k]
    A[k] = A[k] / pivot
    B[k] = B[k] / pivot

    for i in range(n):
        if i != k:
            factor = A[i, k]
            A[i] -= factor * A[k]
            B[i] -= factor * B[k]

print("Gauss-Jordan Solution Vector:")
print(B)
