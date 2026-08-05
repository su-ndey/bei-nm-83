# Lab 5 - Inverse Power Method
# Pure Python - matrices are nested lists, no external libraries needed.
#
# Finds the smallest eigenvalue (in magnitude) of A by applying the Power Method
# to A inverse. Instead of inverting A, the system A.Y = X is solved every
# iteration using Gaussian elimination with partial pivoting.
#
#   lambda_smallest = 1 / mu,  where mu is the dominant eigenvalue of A inverse

A = [
    [4, 1, 0],
    [1, 20, 1],
    [0, 1, 4]
]

A = [[float(value) for value in row] for row in A]
n = len(A)


def solve(matrix, rhs):
    # Solve matrix * y = rhs by Gaussian elimination with partial pivoting.
    # Copies are made so the caller's matrix is never modified.
    n = len(rhs)
    M = [row[:] for row in matrix]
    b = rhs[:]

    for k in range(n - 1):
        max_row = k
        for i in range(k + 1, n):
            if abs(M[i][k]) > abs(M[max_row][k]):
                max_row = i
        M[k], M[max_row] = M[max_row], M[k]
        b[k], b[max_row] = b[max_row], b[k]

        for i in range(k + 1, n):
            factor = M[i][k] / M[k][k]
            for j in range(k, n):
                M[i][j] -= factor * M[k][j]
            b[i] -= factor * b[k]

    y = [0.0] * n
    for i in range(n - 1, -1, -1):
        total = sum(M[i][j] * y[j] for j in range(i + 1, n))
        y[i] = (b[i] - total) / M[i][i]
    return y


def index_of_largest_magnitude(v):
    best = 0
    for i in range(1, len(v)):
        if abs(v[i]) > abs(v[best]):
            best = i
    return best


x = [1.0, 1.0, 1.0]
tolerance = 1e-5
max_iterations = 100
lambda_old = 0.0
lambda_new = 0.0

for iteration in range(max_iterations):

    # Solve A.Y = X instead of computing an explicit inverse
    y = solve(A, x)

    max_idx = index_of_largest_magnitude(y)
    mu = y[max_idx]

    x = [value / mu for value in y]
    lambda_new = 1.0 / mu

    if abs(lambda_new - lambda_old) < tolerance:
        break
    lambda_old = lambda_new

print(f"Smallest Eigenvalue: {lambda_new:.5f}")
print("Corresponding Eigenvector:")
for i in range(n):
    print(f"  x{i + 1} = {x[i]:.6f}")
