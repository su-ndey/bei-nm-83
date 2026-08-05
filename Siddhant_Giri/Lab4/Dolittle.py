import numpy as np

A = np.array([
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 8]
], dtype=float)

b = np.array([-2, 9, -5], dtype=float)

n = len(A)

# Initialize L and U
L = np.eye(n)
U = np.zeros((n, n))

for i in range(n):

    for j in range(i, n):
        s = 0
        for k in range(i):
            s += L[i][k] * U[k][j]
        U[i][j] = A[i][j] - s

    for j in range(i + 1, n):
        s = 0
        for k in range(i):
            s += L[j][k] * U[k][i]

        L[j][i] = (A[j][i] - s) / U[i][i]

print("Lower Matrix (L):")
print(L)

print("\nUpper Matrix (U):")
print(U)

y = np.zeros(n)

for i in range(n):
    s = 0
    for j in range(i):
        s += L[i][j] * y[j]
    y[i] = b[i] - s

x = np.zeros(n)

for i in range(n - 1, -1, -1):
    s = 0
    for j in range(i + 1, n):
        s += U[i][j] * x[j]

    x[i] = (y[i] - s) / U[i][i]

print("\nIntermediate Vector (y):")
print(y)

print("\nSolution Vector (x):")
print(x)