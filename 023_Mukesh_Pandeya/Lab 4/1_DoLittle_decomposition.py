import numpy as np
A = [[2,  1, -1],
     [-3, -1,  2],
     [-2,  1,  2]]

B = [8, -11, -3]

def doolittle(A, B):
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n)) 
    # LU Decomposition using Do Little's method
    for i in range(n):
        for j in range(n):
            if i <= j:
                U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(i))
                L[i][i] = 1
            else:
                L[i][j] = (A[i][j] - sum(L[i][k]*U[k][j] for k in range(j))) / U[j][j]

    # Forward substitution: Ly = B
    y = np.zeros(n)
    for i in range(n):
        y[i] = B[i] - sum(L[i][k]*y[k] for k in range(i))

    # Back substitution: Ux = y
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][k]*x[k] for k in range(i+1, n))) / U[i][i]

    return L, U, x



L, U, x = doolittle(A, B)

print("L:\n", L.astype(int))
print("\nU:\n", U.astype(int))
print("\nSolution x:", x.astype(int))