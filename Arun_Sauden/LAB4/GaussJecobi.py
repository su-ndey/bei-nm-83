import numpy as np

A = np.array([
    [10, 1, 2],
    [2, 10, 3],
    [1, 2, 10]
], dtype=float)

B = np.array([13, 15, 13], dtype=float)

n = len(B)

x_old = np.zeros(n)
tolerance = 1e-5
max_iterations = 100

print("=" * 50)
print("        GAUSS-JACOBI ITERATION METHOD")
print("=" * 50)

print("\nInitial Guess:")
print("x1 = 0.000000, x2 = 0.000000, x3 = 0.000000")

print("\nIteration Results:")
print("-" * 50)
print(f"{'Iteration':<12}{'x1':<12}{'x2':<12}{'x3':<12}{'Error':<12}")
print("-" * 50)

for k in range(max_iterations):
    x_new = np.zeros(n)

    for i in range(n):
        s = 0.0
        for j in range(n):
            if i != j:
                s += A[i, j] * x_old[j]

        x_new[i] = (B[i] - s) / A[i, i]

    error = np.max(np.abs(x_new - x_old))

    print(f"{k+1:<12}{x_new[0]:<12.6f}{x_new[1]:<12.6f}{x_new[2]:<12.6f}{error:<12.6f}")

    if error < tolerance:
        print("-" * 50)
        print(f"Converged after {k + 1} iterations.")
        break

    x_old = np.copy(x_new)

print("-" * 50)
print("Final Jacobi Solution:")
print("-" * 50)

for i in range(n):
    print(f"x{i+1} = {x_new[i]:.6f}")

print("=" * 50)