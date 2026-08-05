import numpy as np

A = np.array([
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 8]
], dtype=float)

B = np.array([-2, 9, -5], dtype=float)

n = len(A)

L = np.eye(n)
U = np.zeros((n, n))

# LU Decomposition
for i in range(n):

    # Upper Triangular Matrix
    for j in range(i, n):
        sum1 = 0

        for k in range(i):
            sum1 += L[i][k] * U[k][j]

        U[i][j] = A[i][j] - sum1

    # Lower Triangular Matrix
    for j in range(i + 1, n):
        sum2 = 0

        for k in range(i):
            sum2 += L[j][k] * U[k][i]

        L[j][i] = (A[j][i] - sum2) / U[i][i]

print("Lower Matrix L:")
print(L)

print("\nUpper Matrix U:")
print(U)

# Forward Substitution (LY = B)
Y = np.zeros(n)

for i in range(n):
    sumy = 0

    for j in range(i):
        sumy += L[i][j] * Y[j]

    Y[i] = B[i] - sumy

# Backward Substitution (UX = Y)
X = np.zeros(n)

for i in range(n - 1, -1, -1):
    sumx = 0

    for j in range(i + 1, n):
        sumx += U[i][j] * X[j]

    X[i] = (Y[i] - sumx) / U[i][i]

print("\nSolution:")
print(X)