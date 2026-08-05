import numpy as np

A = np.array([
    [4, 1, 0],
    [1, 20, 1],
    [0, 1, 4]
], dtype=float)

x = np.array([1.0, 1.0, 1.0], dtype=float)

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

print("Power Method Result")
print("-------------------")
print(f"Dominant Eigenvalue: {lambda_new:.5f}")
print("Corresponding Eigenvector:")

for i in range(len(x)):
    print(f"x{i+1} = {x[i]:.5f}")

print(f"\nIterations: {iteration + 1}")