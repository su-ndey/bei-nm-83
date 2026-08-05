import numpy as np

rows = int(input("Enter the number of rows in the coefficient matrix (A): "))
cols = int(input("Enter the number of columns in the coefficient matrix (A): "))
print("Enter the matrix entries row by row, with entries separated by spaces:")

matrix_entries = []
for i in range(rows):
    row_entries = input(f"Row {i + 1}: ").split()
    matrix_entries.append([float(entry) for entry in row_entries])

A = np.array(matrix_entries, dtype=np.float64)
n = rows

mode = input("Choose method:\n1. Power Method (Dominant Eigenvalue)\n2. Inverse Power Method (Smallest Eigenvalue)\nChoice: ")
num_iterations = int(input("Enter the number of iterations: "))
x = np.ones((n, 1), dtype=np.float64)  # Initial guess for eigenvector

if mode == '1':
    # Power Method (Dominant eigenvalue)
    for _ in range(num_iterations):
        x_new = np.dot(A, x)
        norm = np.linalg.norm(x_new)
        if norm == 0:
            print("The vector became zero. Power method cannot proceed.")
            break
        x = x_new / norm
    Ax = np.dot(A, x)
    numerator = (x.T @ Ax).item()
    denominator = (x.T @ x).item()
    dominant_eigenvalue = numerator / denominator

    print("Dominant Eigenvalue (approx.):", dominant_eigenvalue)
    print("Corresponding Eigenvector (approx.):")
    print(x)
elif mode == '2':
    # Inverse Power Method (Smallest eigenvalue)
    try:
        invA = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        print("Matrix is singular, cannot compute inverse power method.")
        exit(1)
    for _ in range(num_iterations):
        x_new = np.dot(invA, x)
        norm = np.linalg.norm(x_new)
        if norm == 0:
            print("The vector became zero. Inverse power method cannot proceed.")
            break
        x = x_new / norm
    Ax = np.dot(A, x)
    num = (x.T @ Ax).item()
    denom = (x.T @ x).item()
    eigenvalue_approx = num / denom
    if eigenvalue_approx == 0:
        print("Zero division error in eigenvalue computation.")
    else:
        print("Smallest Eigenvalue (approx.):", eigenvalue_approx)
        print("Corresponding Eigenvector (approx.):")
        print(x)
else:
    if mode != '1' and mode != '2':
        print("Invalid choice. Please select 1 (Power Method) or 2 (Inverse Power Method).")
        exit(1)

     
