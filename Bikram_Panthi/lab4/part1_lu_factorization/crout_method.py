# Lab 4 (Part I) - LU Factorization using Crout's Method
# Pure Python - matrices are nested lists, no external libraries needed.
#
# Diagonal elements of U are 1.
# Same system as the Doolittle program.
# Solution obtained: x = -1.875, y = 0.916667, z = -1.333333

A = [
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 8]
]

B = [-2, 9, -5]

A = [[float(value) for value in row] for row in A]
B = [float(value) for value in B]

n = len(A)

# L starts as all zeros, U starts as the identity matrix
L = [[0.0 for j in range(n)] for i in range(n)]
U = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

# LU Decomposition
for j in range(n):

    # Lower Triangular
    for i in range(j, n):

        sum1 = 0.0

        for k in range(j):
            sum1 += L[i][k] * U[k][j]

        L[i][j] = A[i][j] - sum1

    # Upper Triangular
    for i in range(j + 1, n):

        sum2 = 0.0

        for k in range(j):
            sum2 += L[j][k] * U[k][i]

        U[j][i] = (A[j][i] - sum2) / L[j][j]


def show(name, M):
    print(name)
    for row in M:
        print("  " + "  ".join(f"{value:9.4f}" for value in row))


show("Lower Matrix L:", L)
show("Upper Matrix U:", U)

# Forward Substitution  (L Y = B)
Y = [0.0] * n

for i in range(n):

    sumy = 0.0

    for j in range(i):
        sumy += L[i][j] * Y[j]

    Y[i] = (B[i] - sumy) / L[i][i]

# Backward Substitution  (U X = Y, diagonal of U is 1)
X = [0.0] * n

for i in range(n - 1, -1, -1):

    sumx = 0.0

    for j in range(i + 1, n):
        sumx += U[i][j] * X[j]

    X[i] = Y[i] - sumx

print("\nSolution:")
for i in range(n):
    print(f"x{i + 1} = {X[i]:.6f}")
