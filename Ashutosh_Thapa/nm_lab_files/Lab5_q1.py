import numpy as np

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], dtype=float)
B = np.array([8, -11, -3], dtype=float)
n = len(B)

for k in range(n):
  
    max_row = k + np.argmax(np.abs(A[k:, k]))
    if abs(A[max_row, k]) < 1e-12:
        raise ValueError("Matrix is singular or nearly singular.")

    
    A[[k, max_row]] = A[[max_row, k]]
    B[[k, max_row]] = B[[max_row, k]]


    pivot = A[k, k]
    A[k] /= pivot
    B[k] /= pivot


    for i in range(n):
        if i != k:
            factor = A[i, k]
            A[i] -= factor * A[k]
            B[i] -= factor * B[k]

print("Gauss-Jordan Solution Vector:")
print(B)