import numpy as np

A = np.array([
    [10, 1, 2],
    [2, 10, 3],
    [1, 2, 10]
], dtype=float)

B = np.array([13, 15, 13], dtype=float)

n = len(B)

x = np.zeros(n)
tolerance = 1e-5
max_iterations = 100

print("Gauss-Seidel Iteration Steps\n")

print("Iter\t x1\t\t x2\t\t x3\t\t Error")
print("-" * 55)

for k in range(max_iterations):
    x_old = np.copy(x)

    for i in range(n):
        s = 0.0

        for j in range(n):
            if i != j:
                s += A[i, j] * x[j]

        x[i] = (B[i] - s) / A[i, i]

    error = np.max(np.abs(x - x_old))

    print(f"{k+1}\t {x[0]:.6f}\t {x[1]:.6f}\t {x[2]:.6f}\t {error:.6f}")

    if error < tolerance:
        print("\nConverged!")
        break

print("\nFinal Solution:")
print(f"x1 = {x[0]:.6f}")
print(f"x2 = {x[1]:.6f}")
print(f"x3 = {x[2]:.6f}")