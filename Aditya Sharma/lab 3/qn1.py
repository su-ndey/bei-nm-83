import numpy as np

def gauss_elimination_partial_pivoting(A):
    A = A.astype(float)
    n = len(A)
    
    for k in range(n - 1):
        # Find row with largest abs value in column k
        max_row = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[max_row][k]):
                max_row = i
        
        # Swap row k and max_row
        A[[k, max_row]] = A[[max_row, k]]
        print(f"After partial pivot (k={k}), swapped rows {k} & {max_row}:\n{A}\n")
        
        # Elimination
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n + 1):
                A[i][j] = A[i][j] - factor * A[k][j]
    
    return back_substitution(A, n)


def gauss_elimination_complete_pivoting(A):
    A = A.astype(float)
    n = len(A)
    col_order = list(range(n))  # Track column swaps
    
    for k in range(n - 1):
        # Find largest abs value in submatrix A[k:n][k:n]
        max_val = 0
        max_row, max_col = k, k
        for i in range(k, n):
            for j in range(k, n):
                if abs(A[i][j]) > abs(max_val):
                    max_val = A[i][j]
                    max_row, max_col = i, j
        
        # Swap rows and columns
        A[[k, max_row]] = A[[max_row, k]]
        A[:, [k, max_col]] = A[:, [max_col, k]]
        col_order[k], col_order[max_col] = col_order[max_col], col_order[k]
        print(f"After complete pivot (k={k}), swapped rows {k}&{max_row}, cols {k}&{max_col}:\n{A}\n")
        
        # Elimination
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n + 1):
                A[i][j] = A[i][j] - factor * A[k][j]
    
    x = back_substitution(A, n)
    
    # Rearrange solution according to column swaps
    x_final = np.zeros(n)
    for i in range(n):
        x_final[col_order[i]] = x[i]
    return x_final


def back_substitution(A, n):
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    return x


# ─── Main ───────────────────────────────────────────────
# Augmented matrix [A | b]
A = np.array([
    [2,  1, -1,  8],
    [-3, -1,  2, -11],
    [-2,  1,  2, -3]
], dtype=float)

print("=" * 50)
print("PARTIAL PIVOTING")
print("=" * 50)
A_partial = A.copy()
x = gauss_elimination_partial_pivoting(A_partial)
print("Solution:", x)

print("\n" + "=" * 50)
print("COMPLETE PIVOTING")
print("=" * 50)
A_complete = A.copy()
x = gauss_elimination_complete_pivoting(A_complete)
print("Solution:", x)
