import numpy as np

rows = int(input("Enter the number of rows in the coefficient matrix (A): "))
cols = int(input("Enter the number of columns in the coefficient matrix (A): "))
print("Enter the matrix entries row by row, with entries separated by spaces:")

matrix_entries = []
for i in range(rows):
    row_entries = input(f"Row {i + 1}: ").split()
    matrix_entries.append([float(entry) for entry in row_entries])

A = np.array(matrix_entries, dtype=np.float64)

ch = input("Enter which method you want \n 1.Doolittle's method \n 2.Crout's method \n Choice:")

print("Enter the constants entries row by row, with entries separated by spaces:")
constants_entries = []
for i in range(rows):
    row_entries = input(f"Row {i + 1}: ").split()
    constants_entries.append([float(entry) for entry in row_entries])
B = np.array(constants_entries, dtype=np.float64).reshape((rows, 1))

if ch == '1':
    # Doolittle's Method (L: unit lower triangular, U: upper triangular)
    L = np.zeros((rows, cols))
    U = np.zeros((rows, cols))
    for i in range(rows):
        L[i][i] = 1
        for j in range(i, cols):
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]
        for j in range(i + 1, rows):
            L[j][i] = A[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            if U[i][i] == 0:
                print(f"Zero pivot encountered at U[{i}][{i}]. LU decomposition cannot proceed without pivoting.")
                exit(1)
            L[j][i] /= U[i][i]
    print("L:\n", L)
    print("U:\n", U)

    # Forward substitution for L*Y=B
    Y = np.zeros((rows, 1))
    for i in range(rows):
        Y[i] = B[i]
        for j in range(i):
            Y[i] -= L[i][j] * Y[j]

    # Backward substitution for U*X=Y
    X = np.zeros((rows, 1))
    for i in range(rows - 1, -1, -1):
        X[i] = Y[i]
        for j in range(i + 1, rows):
            X[i] -= U[i][j] * X[j]
        if U[i][i] == 0:
            print(f"No unique solution exists due to zero diagonal at U[{i}][{i}].")
            exit(1)
        X[i] /= U[i][i]
    print("The solution is: ", X.round().astype(int).flatten())

elif ch == '2':
    # Crout's Method (L: lower triangular, U: unit upper triangular)
    L = np.zeros((rows, cols))
    U = np.zeros((rows, cols))
    for i in range(rows):
        U[i][i] = 1
        for j in range(i, cols):
            L[i][j] = A[i][j]
            for k in range(i):
                L[i][j] -= L[i][k] * U[k][j]
        for j in range(i + 1, rows):
            U[j][i] = A[j][i]
            for k in range(i):
                U[j][i] -= L[j][k] * U[k][i]
            if L[i][i] == 0:
                print(f"Zero pivot encountered at L[{i}][{i}]. LU decomposition cannot proceed without pivoting.")
                exit(1)
            U[j][i] /= L[i][i]
    print("L:\n", L)
    print("U:\n", U)

    # Forward substitution for L*Y=B
    Y = np.zeros((rows, 1))
    for i in range(rows):
        Y[i] = B[i]
        for j in range(i):
            Y[i] -= L[i][j] * Y[j]
        if L[i][i] == 0:
            print(f"No unique solution exists due to zero diagonal at L[{i}][{i}].")
            exit(1)
        Y[i] /= L[i][i]

    # Backward substitution for U*X=Y
    X = np.zeros((rows, 1))
    for i in range(rows - 1, -1, -1):
        X[i] = Y[i]
        for j in range(i + 1, rows):
            X[i] -= U[i][j] * X[j]
        # In Crout's, U[i][i] = 1 so no need to divide
    print("The solution is: ", X.round().astype(int).flatten())
else:
    print("Invalid choice. Please enter 1 for Doolittle or 2 for Crout.")