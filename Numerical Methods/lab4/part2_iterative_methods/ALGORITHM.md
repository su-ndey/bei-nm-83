# Lab 4 (Part II) - Gauss-Jacobi and Gauss-Seidel - Algorithms

Both methods start from an initial guess (all zeros) and refine it repeatedly.
Convergence is guaranteed when the coefficient matrix is **strictly diagonally
dominant**:

```
|a(i,i)| > Σ |a(i,j)|      for all j ≠ i, in every row
```

If the matrix is not diagonally dominant, the rows should be reordered before
starting, if such an ordering exists.

Tolerance used: `ε = 1e-5`, maximum iterations = 100.

---

## 1. Gauss-Jacobi Method (simultaneous displacement)

Every component of a sweep is computed from the **previous** iteration's values
only, so the whole vector is replaced at once.

```
x_i(k+1) = ( b_i - Σ_{j≠i} a(i,j)·x_j(k) ) / a(i,i)
```

### Algorithm

1. Start.
2. Input the diagonally dominant coefficient matrix `A`, the constant vector `B`,
   the tolerance `ε` and the maximum number of iterations.
3. Verify that every row satisfies the diagonal dominance condition, and warn if it
   does not.
4. Initialise the solution vector `X_old` with zeros.
5. Repeat, up to the maximum number of iterations:
   a. Create a temporary array `X_new` to hold this sweep's values.
   b. For each row `i` from 0 to `n-1`:
      - Compute `sum = Σ A[i][j] × X_old[j]` for all `j ≠ i`.
      - Compute `X_new[i] = ( B[i] - sum ) / A[i][i]`.
   c. Compute the error as the largest value of `|X_new[i] - X_old[i]|`.
   d. Copy `X_new` into `X_old`.
   e. If the error is less than `ε`, stop iterating.
6. Display the solution vector.
7. Stop.

### Pseudocode

```
BEGIN

Input A, B, tolerance, max_iterations
X_old = zeros

FOR k = 1 TO max_iterations

    FOR each row i
        sum = Σ A[i][j] * X_old[j]      for j != i
        X_new[i] = (B[i] - sum) / A[i][i]
    END FOR

    error = max( abs(X_new[i] - X_old[i]) )
    X_old = X_new

    IF error < tolerance THEN
        PRINT "Converged in", k, "iterations"
        STOP
    END IF

END FOR

END
```

---

## 2. Gauss-Seidel Method (successive displacement)

Each new value is used immediately within the same sweep, so components computed
earlier in the sweep already contribute their updated values.

```
x_i(k+1) = ( b_i - Σ_{j<i} a(i,j)·x_j(k+1) - Σ_{j>i} a(i,j)·x_j(k) ) / a(i,i)
```

### Algorithm

1. Start.
2. Input the diagonally dominant matrix `A`, the vector `B`, the tolerance `ε` and
   the maximum number of iterations.
3. Verify the diagonal dominance condition and warn if any row fails it.
4. Initialise the solution vector `X` with zeros.
5. Repeat, up to the maximum number of iterations:
   a. Save a tracking copy `X_old = X`, used only to measure the error.
   b. For each row `i` from 0 to `n-1`:
      - Compute `sum = Σ A[i][j] × X[j]` for all `j ≠ i`. The terms with `j < i`
        automatically use the values already updated in this sweep.
      - Overwrite the entry directly: `X[i] = ( B[i] - sum ) / A[i][i]`.
   c. Compute the error as the largest value of `|X[i] - X_old[i]|`.
   d. If the error is less than `ε`, stop iterating.
6. Display the solution vector `X`.
7. Stop.

### Pseudocode

```
BEGIN

Input A, B, tolerance, max_iterations
X = zeros

FOR k = 1 TO max_iterations

    X_old = copy of X

    FOR each row i
        sum = Σ A[i][j] * X[j]          for j != i, using the current X
        X[i] = (B[i] - sum) / A[i][i]
    END FOR

    error = max( abs(X[i] - X_old[i]) )

    IF error < tolerance THEN
        PRINT "Converged in", k, "iterations"
        STOP
    END IF

END FOR

END
```

### Difference between the two

The only structural difference is that Gauss-Jacobi writes into a separate array
`X_new` and swaps it in at the end of the sweep, while Gauss-Seidel writes back into
`X` immediately. That single change is what makes Gauss-Seidel converge in roughly
half the number of iterations.
