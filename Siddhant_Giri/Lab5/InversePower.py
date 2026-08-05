import numpy as np
A = np.array([
    [4, 1, 0],
    [1, 20, 1],
    [0 ,1 , 4]
],dtype=float)
x = np.array([1.0, 1.0, 1.0],dtype=float)
tolerance = 1e-5
max_iterations = 100
lambda_old = 0.0    
for iteration in range(max_iterations):
    y = np.linalg.solve(A, x)
    max_index = np.argmax(np.abs(y))
    mu = y[max_index]
    x = y / mu
    lambda_new = 1.0 / mu
    if abs(lambda_new - lambda_old) < tolerance:
        break
    lambda_old = lambda_new
print(f"Dominant eigenvalue: {lambda_new:.5f}")     
print(f"Corresponding eigenvector: {x}")       