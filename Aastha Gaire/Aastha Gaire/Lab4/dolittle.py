import numpy as np

def doolittle(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # LU Decomposition
    for i in range(n):
        for j in range(n):
            if i <= j:
                U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(i))
                L[i][i] = 1
            else:
                L[i][j] = (A[i][j] - sum(L[i][k]*U[k][j] for k in range(j))) / U[j][j]

    # Forward substitution: Ly = b
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i][k]*y[k] for k in range(i))

    # Back substitution: Ux = y
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][k]*x[k] for k in range(i+1, n))) / U[i][i]

    return L, U, x


# Example
A = [[2,  1, -1],
     [-3, -1,  2],
     [-2,  1,  2]]

b = [8, -11, -3]

L, U, x = doolittle(A, b)

print("L:\n", L)
print("\nU:\n", U)
print("\nSolution x:", x) 