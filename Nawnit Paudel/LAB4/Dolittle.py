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

for i in range(n):

    for k in range(i, n):
        U[i, k] = A[i, k] - sum(L[i, j] * U[j, k] for j in range(i))

    for k in range(i + 1, n):
        L[k, i] = (A[k, i] - sum(L[k, j] * U[j, i] for j in range(i))) / U[i, i]

print("Lower Matrix =")
print(L) 

print("Upper Matrix =")
print(U)

y = np.zeros(n)
for i in range(n):
    y[i] = B[i] - sum(L[i, j] * y[j] for j in range(i))

x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (y[i] - sum(U[i, j] * x[j] for j in range(i + 1, n))) / U[i, i]

print("Solution x =")
print(x)