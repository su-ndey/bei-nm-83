import numpy as np

A = np.array([[4, 1, 0], [1, 20, 1], [0, 1, 4]], dtype=float)
x = np.array([1.0, 1.0, 1.0], dtype=float)
tolerance = 1e-5
max_iterations = 100
lambda_old = 0.0

for iteration in range(1, max_iterations + 1):
    y = np.linalg.solve(A, x)
    max_idx = np.argmax(np.abs(y))
    mu = y[max_idx]
    x = y / mu
    lambda_new = 1.0 / mu
    if abs(lambda_new - lambda_old) < tolerance:
        print(f"Converged in {iteration} iterations.\n")
        break
    lambda_old = lambda_new
else:
    print("Reached max iterations without convergence.\n")
    
print(f"Smallest Eigenvalue: {lambda_new:.5f}")
print("Corresponding Eigenvector:", x)