import numpy as np

A = np.array([[4, 1, 0],
              [1, 20, 1],
              [0, 1, 4]], dtype=float)

x = np.array([1.0, 1.0, 1.0], dtype=float)
tolerance = 1e-5
max_iterations = 100
lamda_old = 0

for iteration in range(max_iterations):
    y = np.dot(A, x)
    max_idx = np.argmax(np.abs(y))
    lamda_new = y[max_idx]
    x = y / lamda_new

    if abs(lamda_new - lamda_old) < tolerance:
        break

    lamda_old = lamda_new

print("Dominant Eigenvalue:", lamda_new)
print("Eigenvector:", x)