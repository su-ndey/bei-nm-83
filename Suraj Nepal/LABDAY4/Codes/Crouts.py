import numpy as np

A = np.array([
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 8]
], dtype=float)

B = np.array([-2, 9, -5], dtype=float)

n = len(A)

L = np.zeros((n, n))
U = np.eye(n)

for j in range(n):

    for i in range(j, n):
        L[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(j))

    for i in range(j + 1, n):
        U[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(j))) / L[j, j]

print("Lower Matrix (L) =")
print(L)

print("Upper Matrix (U) =")
print(U)

y = np.zeros(n)
for i in range(n):
    y[i] = (B[i] - sum(L[i, j] * y[j] for j in range(i))) / L[i, i]

x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = y[i] - sum(U[i, j] * x[j] for j in range(i + 1, n))

print("Solution x =")
print(x)