import numpy as np

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
B = np.array(constants_entries, dtype=np.float64).reshape((rows, 1))
tolerance=int(input("Enter the tolerance for convergence: "))
max_iterations=int(input("Enter the maximum number of iterations: "))
for i in range(max_iterations):
    x_new=np.copy(B)
    for j in range(rows):
        sum_ax=np.dot(A[j,:j],x_new[:j]) + np.dot(A[j,j+1:],B[j+1:])
        x_new[j]=(B[j]-sum_ax)/A[j,j]
    if np.linalg.norm(x_new-B, ord=np.inf) < tolerance:
        print(f"Convergence achieved after {i+1} iterations.")
        break
    B=np.copy(x_new)
else:
    print("Maximum iterations reached without convergence.")
print("The solution is: ", x_new.round().astype(int))