import numpy as np

A = np.array([
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 8]
], dtype=float)

B = np.array([-2, 9, -5], dtype=float)

size = len(A)

L = np.eye(size)
U = np.zeros((size, size))

# LU Decomposition (Doolittle)
for row in range(size):

    for col in range(row, size):
        value = np.dot(L[row, :row], U[:row, col])
        U[row, col] = A[row, col] - value

    for col in range(row + 1, size):
        value = np.dot(L[col, :row], U[:row, row])
        L[col, row] = (A[col, row] - value) / U[row, row]

print("Lower Matrix L:")
print(L)

print("\nUpper Matrix U:")
print(U)

Y = np.zeros(size)

for i in range(size):
    value = np.dot(L[i, :i], Y[:i])
    Y[i] = B[i] - value

X = np.zeros(size)

for i in range(size - 1, -1, -1):
    value = np.dot(U[i, i + 1:], X[i + 1:])
    X[i] = (Y[i] - value) / U[i, i]

print("\nSolution:")
print(X)