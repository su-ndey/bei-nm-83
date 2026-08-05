import numpy as np

# Coefficient matrix
A = np.array([
    [4, 1, 0],
    [1, 20, 1],
    [0, 1, 4]
], dtype=float)

# Initial guess for the eigenvector
x = np.array([1.0, 1.0, 1.0], dtype=float)

# Parameters
tolerance = 1e-5
max_iterations = 100
lambda_old = 0.0

# Power Method
for iteration in range(max_iterations):

    # Multiply matrix by the current vector
    y = np.dot(A, x)

    # Find the largest absolute value component
    max_index = np.argmax(np.abs(y))
    lambda_new = y[max_index]

    # Normalize the vector
    x = y / lambda_new

    # Check for convergence
    if abs(lambda_new - lambda_old) < tolerance:
        break

    lambda_old = lambda_new

# Display the results
print("Dominant Eigenvalue:", round(lambda_new, 5))
print("Corresponding Eigenvector:")
print(x)
