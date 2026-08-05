import numpy as np

A = [[2,  1, -1],
     [-3, -1,  2],
     [-2,  1,  2]]

B = [8, -11, -3]

def crout(A, B):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # LU Decomposition using Crout's method
    for j in range(n):
        # Calculate L column
        for i in range(j, n):
            L[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(j))
        
        U[j][j] = 1
        
        for i in range(j+1, n):
            U[j][i] = (A[j][i] - sum(L[j][k]*U[k][i] for k in range(j))) / L[j][j]

    y = np.zeros(n)
    for i in range(n):
        y[i] = B[i] - sum(L[i][k]*y[k] for k in range(i))
        y[i] = y[i] / L[i][i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = y[i] - sum(U[i][k]*x[k] for k in range(i+1, n))

    return L, U, x

L, U, x = crout(A, B)

print("L:\n", L.astype(int))
print("\nU:\n", U.astype(int))
print("\nSolution x:", x.astype(int))
