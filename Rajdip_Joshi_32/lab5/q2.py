#power method
import numpy as np

# Matrix definition
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

# Power Method
for iteration in range(max_iterations):
    y = np.dot(A, x)

    # Find the largest absolute value
    max_idx = np.argmax(np.abs(y))
    lambda_new = y[max_idx]

    # Normalize the vector
    x = y / lambda_new

    # Check for convergence
    if abs(lambda_new - lambda_old) < tolerance:
        break

    lambda_old = lambda_new

# Display results
print(f"Dominant Eigenvalue: {lambda_new:.5f}")
print("Corresponding Eigenvector:", x)
