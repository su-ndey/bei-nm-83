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

print("Gauss-Seidel Iteration Steps:")

for k in range(max_iterations):
    x_old = np.copy(x)

    for i in range(n):
        s = 0.0
        for j in range(n):
            if i != j:
                s += A[i, j] * x[j]  

        x[i] = (B[i] - s) / A[i, i]

    error = np.max(np.abs(x - x_old))

    print(f"Iteration {k+1}: {x}, Error: {error:.6f}")

    if error < tolerance:
        print(f"Converged in {k+1} iterations.")
        break

print("Final Seidel Solution:", x)