# Lab 3 - Gaussian Elimination with Pivoting - Algorithms

Both methods solve `AX = B` by reducing `A` to upper triangular form and then
applying back substitution. Pivoting chooses a large pivot element so that the
division does not amplify round-off error.

**Back substitution formulas**

```
x(n) = b(n) / a(n,n)
x(i) = ( b(i) - Σ a(i,j)·x(j) ) / a(i,i)        for j > i
```

---

## 1. Gaussian Elimination with Partial Pivoting

Only rows are swapped, so the order of the variables never changes.

### Algorithm

1. Start.
2. Input the coefficient matrix `A` and the constant vector `B`.
3. Form the augmented matrix `[A | B]`.
4. For each pivot column `k` from 0 to `n-2`:
   a. Search rows `k` to `n-1` for the entry with the largest absolute value in
      column `k`; call that row `max_row`.
   b. Swap row `k` with row `max_row` in both `A` and `B`.
   c. For each row `i` below the pivot:
      - Compute `factor = A[i][k] / A[k][k]`.
      - Subtract `factor × row k` from row `i`, for columns `k` to `n-1`.
      - Subtract `factor × B[k]` from `B[i]`.
5. The matrix is now upper triangular. Apply back substitution to find `X`.
6. Display the solution.
7. Stop.

### Pseudocode

```
BEGIN

FOR each column k

    Find the row with the largest absolute pivot in column k
    Swap that row with row k

    FOR each row i below the pivot
        factor = A[i][k] / A[k][k]
        Eliminate the entries below the pivot
    END FOR

END FOR

Perform back substitution

END
```

---

## 2. Gaussian Elimination with Complete Pivoting

The largest element in the whole remaining submatrix is used as the pivot, so both
rows **and columns** are swapped. Because swapping columns reorders the unknowns,
the swaps must be recorded and undone at the end.

### Algorithm

1. Start.
2. Input the matrix `A` and the vector `B`.
3. Create a list `col_index = [0, 1, ..., n-1]` to record the column order.
4. For each pivot step `k` from 0 to `n-2`:
   a. Search the submatrix `A[k:][k:]` for the entry with the largest absolute
      value; note its row and column.
   b. Swap that row with row `k` in both `A` and `B`.
   c. Swap that column with column `k` in `A`, and swap the corresponding entries of
      `col_index`.
   d. For each row `i` below the pivot:
      - Compute `factor = A[i][k] / A[k][k]`.
      - Eliminate the entries below the pivot in row `i`, and update `B[i]`.
5. Apply back substitution to obtain the vector `x`.
6. Rearrange the variables: for each `i`, set `solution[col_index[i]] = x[i]`.
7. Display the solution.
8. Stop.

### Pseudocode

```
BEGIN

col_index = [0, 1, ..., n-1]

FOR each pivot step k

    Find the largest absolute element in the submatrix A[k:][k:]

    Swap rows
    Swap columns and record the swap in col_index

    Perform elimination below the pivot

END FOR

Perform back substitution

Rearrange the variables using col_index

END
```

### Note on step 6

Without the rearrangement in step 6 the computed values come out attached to the
wrong unknowns, because every column swap has exchanged two variables.
