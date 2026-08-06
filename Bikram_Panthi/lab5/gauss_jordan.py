# Lab 5 - Gauss-Jordan Elimination Method
# Pure Python - matrices are nested lists, no external libraries needed.
#
# The augmented matrix [A | B] is reduced directly to [I | X], so no separate
# back-substitution step is needed.
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

A = [[float(value) for value in row] for row in A]
B = [float(value) for value in B]

n = len(B)

# Gauss-Jordan: eliminate below AND above every pivot
for k in range(n):

    # Partial pivoting to handle zero (or near-zero) pivots
    if abs(A[k][k]) < 1e-12:
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[k][k]):
                A[k], A[i] = A[i], A[k]
                B[k], B[i] = B[i], B[k]
                break

    # Make the pivot equal to 1
    pivot = A[k][k]
    for j in range(n):
        A[k][j] /= pivot
    B[k] /= pivot

    # Clear column k in every other row
    for i in range(n):
        if i != k:
            factor = A[i][k]
            for j in range(n):
                A[i][j] -= factor * A[k][j]
            B[i] -= factor * B[k]

print("Reduced matrix (should be the identity):")
for row in A:
    print("  " + "  ".join(f"{value:7.4f}" for value in row))

print("\nGauss-Jordan Solution Vector:")
for i in range(n):
    print(f"x{i + 1} = {B[i]:.6f}")
