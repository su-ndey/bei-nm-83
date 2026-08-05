# Lab 4 (Part II) - Gauss-Seidel Iterative Method
# Pure Python - matrices are nested lists, no external libraries needed.
#
# Uses the most recently updated values inside the same sweep, so it usually
# converges in about half the iterations of Gauss-Jacobi.
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

x = [0.0] * n
tolerance = 1e-5
max_iterations = 100

print("Gauss-Seidel Iteration Steps:")
for k in range(max_iterations):

    x_old = list(x)          # tracking copy, only used to measure the error

    for i in range(n):
        s = 0.0
        for j in range(n):
            if i != j:
                s += A[i][j] * x[j]      # uses the current, updated x directly
        x[i] = (B[i] - s) / A[i][i]

    error = max(abs(x[i] - x_old[i]) for i in range(n))

    values = ", ".join(f"{value:.6f}" for value in x)
    print(f"Iteration {k + 1}: [{values}], Error: {error:.6f}")

    if error < tolerance:
        print(f"Converged in {k + 1} iterations.")
        break

print("\nFinal Seidel Solution:")
for i in range(n):
    print(f"x{i + 1} = {x[i]:.6f}")
