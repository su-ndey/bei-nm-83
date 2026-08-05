import numpy as np
A = np.array([[10, 1, 2],
              [2, 10, 3],
              [1, 2, 10]], dtype=float)
b = np.array([13, 15, 14], dtype=float)
n = len(b)
x_old = np.zeros(n)
tolerance = 1e-5
max_iterations = 100
for k in range(max_iterations):
    x_new = np.zeros(n)
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += A[i][j] * x_old[j]
        x_new[i] = (b[i] - s) / A[i][i]
    error = np.max(np.abs(x_new - x_old))
    print(f"Iteration {k+1}: x = {x_new}, error = {error}")
    if error < tolerance:
        print("Convergence achieved.")
        x_old = x_new
        break
    x_old = x_new
print("Final solution is :\n", x_new)
        
              