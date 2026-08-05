import numpy as np

# Input matrix A and vector B
rows = int(input("Enter the number of rows in the coefficient matrix (A): "))
cols = int(input("Enter the number of columns in the coefficient matrix (A): "))
print("Enter the matrix entries row by row, with entries separated by spaces:")
mat_entries = []
for i in range(rows):
    row_entries = input(f"Row {i + 1}: ").split()
    mat_entries.append([float(entry) for entry in row_entries])
A = np.array(mat_entries, dtype=np.float64)

print("Enter the constants entries row by row, with entries separated by spaces:")
constants_entries = []
for i in range(rows):
    row_entries = input(f"Row {i + 1}: ").split()
    constants_entries.append([float(entry) for entry in row_entries])
B = np.array(constants_entries, dtype=np.float64).flatten()

tolerance = float(input("Enter the tolerance for convergence: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

x_old = np.zeros(rows)
x_new = np.zeros(rows)

for iteration in range(1, max_iterations + 1):
    for i in range(rows):
        sum1 = np.dot(A[i, :i], x_old[:i])  # sum for known x values from previous iteration
        sum2 = np.dot(A[i, i+1:], x_old[i+1:])  # sum for known x values from previous iteration
        x_new[i] = (B[i] - sum1 - sum2) / A[i, i]
    if np.linalg.norm(x_new - x_old, ord=np.inf) < tolerance:
        print(f"Convergence achieved after {iteration} iterations.")
        break
    x_old[:] = x_new
else:
    print("Maximum iterations reached without convergence.")

print("The solution is: ", x_new.round().astype(int))