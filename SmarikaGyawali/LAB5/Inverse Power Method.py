import numpy as np

A = np.array([
    [4, 1, 0],
    [1, 20, 1],
    [0, 1, 4]
], dtype=float)

# Initial guess vector
x = np.array([1.0, 1.0, 1.0], dtype=float)

tolerance = 1e-5
max_iterations = 100

lambda_old = 0.0

for iteration in range(max_iterations):

    # Solve A.Y = X instead of calculating inverse
    y = np.linalg.solve(A, x)

    # Find maximum absolute value
    max_idx = np.argmax(np.abs(y))

    # Normalize eigenvector
    mu = y[max_idx]
    x = y / mu

    # Smallest eigenvalue
    lambda_new = 1.0 / mu

    # Check convergence
    if abs(lambda_new - lambda_old) < tolerance:
        break

    lambda_old = lambda_new

print(f"Smallest Eigenvalue: {lambda_new:.5f}")
print("Corresponding Eigenvector:")
print(x)