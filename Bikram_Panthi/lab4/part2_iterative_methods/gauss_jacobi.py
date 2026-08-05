# Lab 4 (Part II) - Gauss-Jacobi Iterative Method
# Pure Python - matrices are nested lists, no external libraries needed.
#
# The coefficient matrix must be strictly diagonally dominant (SDD).
#
# System: 10x +   y +  2z = 13
#          2x + 10y +  3z = 15
#           x +  2y + 10z = 13
# Solution: x = y = z = 1

A = [
    [10, 1, 2],
    [2, 10, 3],
    [1, 2, 10]
]

B = [13, 15, 13]

A = [[float(value) for value in row] for row in A]
B = [float(value) for value in B]

n = len(B)

# Check strict diagonal dominance before iterating
for i in range(n):
    off_diagonal = sum(abs(A[i][j]) for j in range(n) if j != i)
    if abs(A[i][i]) <= off_diagonal:
        print(f"Warning: row {i + 1} is not diagonally dominant - "
              "convergence is not guaranteed.")

x_old = [0.0] * n
tolerance = 1e-5
max_iterations = 100

print("Gauss-Jacobi Iteration Steps:")
for k in range(max_iterations):

    x_new = [0.0] * n

    for i in range(n):
        s = 0.0
        for j in range(n):
            if i != j:
                s += A[i][j] * x_old[j]           # only OLD values are used
        x_new[i] = (B[i] - s) / A[i][i]

    # Maximum absolute error between this sweep and the previous one
    error = max(abs(x_new[i] - x_old[i]) for i in range(n))

    values = ", ".join(f"{value:.6f}" for value in x_new)
    print(f"Iteration {k + 1}: [{values}], Error: {error:.6f}")

    x_old = list(x_new)

    if error < tolerance:
        print(f"Converged in {k + 1} iterations.")
        break

print("\nFinal Jacobi Solution:")
for i in range(n):
    print(f"x{i + 1} = {x_old[i]:.6f}")
