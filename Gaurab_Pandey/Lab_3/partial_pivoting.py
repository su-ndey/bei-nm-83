import numpy as np

A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
], dtype=float)

B = np.array([8, -11, -3], dtype=float)

size = len(B)

for k in range(size - 1):

    pivot = k + np.argmax(np.abs(A[k:, k]))

    A[[k, pivot], :] = A[[pivot, k], :]
    B[[k, pivot]] = B[[pivot, k]]

    for i in range(k + 1, size):

        ratio = A[i, k] / A[k, k]

        A[i, k:] = A[i, k:] - ratio * A[k, k:]
        B[i] = B[i] - ratio * B[k]

solution = np.zeros(size)

for i in range(size - 1, -1, -1):

    total = np.dot(A[i, i + 1:], solution[i + 1:])
    solution[i] = (B[i] - total) / A[i, i]

if np.allclose(solution, np.round(solution)):
    result = np.round(solution).astype(int)
else:
    result = solution

print("Solution:")
print(result)