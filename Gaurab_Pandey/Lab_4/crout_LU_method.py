import numpy as np

A = np.array([
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 8]
], dtype=float)

B = np.array([-2, 9, -5], dtype=float)

size = len(A)

L = np.zeros((size, size))
U = np.eye(size)

for col in range(size):

    for row in range(col, size):
        value = np.dot(L[row, :col], U[:col, col])
        L[row, col] = A[row, col] - value

    for row in range(col + 1, size):
        value = np.dot(L[col, :col], U[:col, row])
        U[col, row] = (A[col, row] - value) / L[col, col]

print("Lower Matrix L:")
print(L)

print("\nUpper Matrix U:")
print(U)

Y = np.zeros(size)

for i in range(size):
    value = np.dot(L[i, :i], Y[:i])
    Y[i] = (B[i] - value) / L[i, i]

X = np.zeros(size)

for i in range(size - 1, -1, -1):
    value = np.dot(U[i, i + 1:], X[i + 1:])
    X[i] = Y[i] - value

print("\nSolution:")
print(X)