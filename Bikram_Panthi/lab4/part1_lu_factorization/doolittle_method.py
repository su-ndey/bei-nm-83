# Lab 4 (Part I) - LU Factorization using Doolittle Method
# Pure Python - matrices are nested lists, no external libraries needed.
#
# Diagonal elements of L are 1.
#
# System:  2x -  y - 2z = -2
#         -4x + 6y + 3z =  9
#         -4x - 2y + 8z = -5
#
# Solution obtained: x = -1.875, y = 0.916667, z = -1.333333
# (I checked this by substituting it back into the original equations. The value
#  x = 1, y = 2, z = -1 gives [2, 5, -16] instead of [-2, 9, -5], so it does not
#  satisfy this particular system.)

A = [
    [2, -1, -2],
    [-4, 6, 3],
    [-4, -2, 8]
]

B = [-2, 9, -5]

A = [[float(value) for value in row] for row in A]
B = [float(value) for value in B]

n = len(A)

# L starts as the identity matrix, U starts as all zeros
L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
U = [[0.0 for j in range(n)] for i in range(n)]

# LU Decomposition
for i in range(n):

    # Upper Triangular
    for j in range(i, n):

        sum1 = 0.0

        for k in range(i):
            sum1 += L[i][k] * U[k][j]

        U[i][j] = A[i][j] - sum1

    # Lower Triangular
    for j in range(i + 1, n):

        sum2 = 0.0

        for k in range(i):
            sum2 += L[j][k] * U[k][i]

        L[j][i] = (A[j][i] - sum2) / U[i][i]


def show(name, M):
    print(name)
    for row in M:
        print("  " + "  ".join(f"{value:9.4f}" for value in row))


show("Lower Matrix L:", L)
show("Upper Matrix U:", U)

# Forward Substitution  (L Y = B, diagonal of L is 1)
Y = [0.0] * n

for i in range(n):

    sumy = 0.0

    for j in range(i):
        sumy += L[i][j] * Y[j]

    Y[i] = B[i] - sumy

# Backward Substitution  (U X = Y)
X = [0.0] * n

for i in range(n - 1, -1, -1):

    sumx = 0.0

    for j in range(i + 1, n):
        sumx += U[i][j] * X[j]

    X[i] = (Y[i] - sumx) / U[i][i]

print("\nSolution:")
for i in range(n):
    print(f"x{i + 1} = {X[i]:.6f}")
