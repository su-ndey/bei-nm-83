import numpy as np

A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)

B = np.array([8, -11, -3], dtype=float)

n = len(B)

for k in range(n):
    p = k
    for i in range(k + 1, n):
        if abs(A[i, k]) > abs(A[p, k]):
            p = i

    if p != k:
        A[[k, p]] = A[[p, k]]
        B[[k, p]] = B[[p, k]]

    pivot = A[k, k]
    A[k] /= pivot
    B[k] /= pivot

    for i in range(n):
        if i != k:
            factor = A[i, k]
            A[i] -= factor * A[k]
            B[i] -= factor * B[k]

print(B)