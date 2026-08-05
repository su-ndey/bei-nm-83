import numpy as np

A = np.array([[2, -1, -2],
              [-4, 6, 3],
              [-4, -2, 8]], dtype=float)

B = np.array([-2, 9, -5], dtype=float)

n = len(A)

L = np.zeros((n, n))
U = np.eye(n)

for j in range(n):
    for i in range(j, n):
        sum1 = 0
        for k in range(j):
            sum1 += L[i][k] * U[k][j]
        L[i][j] = A[i][j] - sum1

    for i in range(j + 1, n):
        sum2 = 0
        for k in range(j):
            sum2 += L[j][k] * U[k][i]
        U[j][i] = (A[j][i] - sum2) / L[j][j]

print("Lower Matrix L:")
print(L)

print("Upper Matrix U:")
print(U)

Y = np.zeros(n)

for i in range(n):
    sumy = 0
    for j in range(i):
        sumy += L[i][j] * Y[j]
    Y[i] = (B[i] - sumy) / L[i][i]

print("Y =", Y)

X = np.zeros(n)

for i in range(n - 1, -1, -1):
    sumx = 0
    for j in range(i + 1, n):
        sumx += U[i][j] * X[j]
    X[i] = Y[i] - sumx

print("Solution X:")
print(X)