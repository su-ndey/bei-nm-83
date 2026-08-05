import numpy as np

A = np.array([
    [4, 1, 0],
    [1, 20, 1],
    [0, 1, 4]
], dtype=float)

x = np.array([1.0, 1.0, 1.0])

tolerance = 1e-5
max_iterations = 100
lambda_old = 0.0

for iteration in range(max_iterations):
    y = np.dot(A, x)

    lambda_new = np.max(np.abs(y))

    x = y / lambda_new

    if abs(lambda_new - lambda_old) < tolerance:
        break

    lambda_old = lambda_new

print("Dominant Eigenvalue =", round(lambda_new, 5))
print("Corresponding Eigenvector =", x)
print("Number of iterations =", iteration + 1)