# Lab 3 - Gaussian Elimination with Partial Pivoting
# Pure Python - matrices are nested lists, no external libraries needed.
#
# System:  2x +  y -  z =   8
#         -3x -  y + 2z = -11
#         -2x +  y + 2z =  -3
# Solution: x = 2, y = 3, z = -1

A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]

B = [8, -11, -3]

# Work with floats so the divisions are exact
A = [[float(value) for value in row] for row in A]
B = [float(value) for value in B]

n = len(B)

# Forward Elimination with Partial Pivoting
for k in range(n - 1):

    # Find the pivot row: largest absolute value in column k, at or below row k
    max_row = k
    for i in range(k + 1, n):
        if abs(A[i][k]) > abs(A[max_row][k]):
            max_row = i

    # Swap rows
    A[k], A[max_row] = A[max_row], A[k]
    B[k], B[max_row] = B[max_row], B[k]

    # Elimination
    for i in range(k + 1, n):

        factor = A[i][k] / A[k][k]

        for j in range(k, n):
            A[i][j] -= factor * A[k][j]

        B[i] -= factor * B[k]

# Back Substitution
x = [0.0] * n

for i in range(n - 1, -1, -1):

    sum_ax = 0.0

    for j in range(i + 1, n):
        sum_ax += A[i][j] * x[j]

    x[i] = (B[i] - sum_ax) / A[i][i]

print("Upper triangular matrix:")
for row in A:
    print([round(value, 4) for value in row])

print("\nSolution:")
for i in range(n):
    print(f"x{i + 1} = {x[i]:.6f}")
