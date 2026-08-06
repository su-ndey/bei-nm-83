# Lab 5 - Gauss-Jordan, Power and Inverse Power Methods - Algorithms

---

## 1. Gauss-Jordan Elimination Method

The augmented matrix is reduced all the way to the identity, so the solution can be
read directly without back substitution:

```
[A | B]  --(elementary row operations)-->  [I | X]
```

### Algorithm

1. Start.
2. Accept the matrix `A` and the constant vector `B`.
3. Form the augmented matrix `[A | B]`.
4. For each pivot index `k` from 0 to `n-1`:
   a. If `|A[k][k]|` is close to zero, swap row `k` with a row below that has a
      non-zero entry in column `k`.
   b. Divide the whole of row `k` (and `B[k]`) by the pivot `A[k][k]`, so the
      diagonal entry becomes 1.
   c. For every other row `i ≠ k`, subtract `A[i][k] × row k` from row `i`, and
      subtract `A[i][k] × B[k]` from `B[i]`, so column `k` becomes zero everywhere
      except at the pivot.
5. Repeat until all columns are processed. `B` now holds the solution vector `X`.
6. Display the solution.
7. Stop.

### Pseudocode

```
BEGIN

FOR each pivot k

    IF A[k][k] is nearly zero THEN
        Swap with a lower row having a non-zero entry in column k
    END IF

    Divide row k by A[k][k]

    FOR every other row i
        factor = A[i][k]
        row i = row i - factor * row k
    END FOR

END FOR

PRINT B as the solution

END
```

---

## 2. Power Method

Finds the eigenvalue of largest magnitude and its eigenvector. Repeated
multiplication by `A` amplifies the dominant eigendirection, and normalising each
step keeps the numbers stable:

```
X(k+1) = A · X(k)
```

The eigenvalue estimate can be cross-checked with the **Rayleigh quotient**:

```
λ = ( Xᵀ A X ) / ( Xᵀ X )
```

### Algorithm

1. Start.
2. Input the matrix `A`, an initial guess vector `X` (I used all ones), the maximum
   number of iterations and the tolerance `ε`.
3. Initialise `λ_old = 0`.
4. Repeat, up to the maximum number of iterations:
   a. Compute `Y = A · X`.
   b. Find `λ_new = Y[m]`, where `|Y[m]|` is the largest absolute value in `Y`.
   c. Normalise for the next step: `X = Y / λ_new`.
   d. Compute the error `|λ_new - λ_old|`.
   e. If the error is less than `ε`, stop iterating; otherwise set `λ_old = λ_new`.
5. Display the dominant eigenvalue `λ_new` and the normalised eigenvector `X`.
6. Stop.

### Pseudocode

```
BEGIN

Input A, X, tolerance, max_iterations
lambda_old = 0

FOR k = 1 TO max_iterations

    Y = A * X
    m = index of the largest absolute component of Y
    lambda_new = Y[m]
    X = Y / lambda_new

    IF abs(lambda_new - lambda_old) < tolerance THEN
        STOP
    END IF

    lambda_old = lambda_new

END FOR

PRINT lambda_new, X

END
```

---

## 3. Inverse Power Method

Finds the eigenvalue of **smallest** magnitude. If `A` has eigenvalue `λ`, then
`A⁻¹` has eigenvalue `1/λ`, so applying the Power Method to `A⁻¹` isolates the
smallest eigenvalue of `A`:

```
λ_smallest = 1 / λ_max(A⁻¹)
```

Rather than computing an explicit inverse, the system `A · Y = X` is solved at each
iteration, which is equivalent to `Y = A⁻¹X` and much cheaper.

### Algorithm

1. Start.
2. Input the matrix `A`, an initial guess vector `X`, the maximum number of
   iterations and the tolerance `ε`.
3. Initialise `λ_old = 0`.
4. Repeat, up to the maximum number of iterations:
   a. Solve the linear system `A · Y = X` for `Y` (I used Gaussian elimination with
      partial pivoting, as implemented in Lab 3).
   b. Find `μ = Y[m]`, where `|Y[m]|` is the largest absolute value in `Y`.
   c. Normalise the vector: `X = Y / μ`.
   d. Compute the eigenvalue estimate `λ_new = 1 / μ`.
   e. If `|λ_new - λ_old| < ε`, stop iterating; otherwise set `λ_old = λ_new`.
5. Display the smallest eigenvalue `λ_new` and the normalised eigenvector `X`.
6. Stop.

### Pseudocode

```
BEGIN

Input A, X, tolerance, max_iterations
lambda_old = 0

FOR k = 1 TO max_iterations

    Solve A * Y = X for Y
    m = index of the largest absolute component of Y
    mu = Y[m]
    X = Y / mu
    lambda_new = 1 / mu

    IF abs(lambda_new - lambda_old) < tolerance THEN
        STOP
    END IF

    lambda_old = lambda_new

END FOR

PRINT lambda_new, X

END
```

### Requirement

`A` must be non-singular. If 0 is an eigenvalue of `A` the method breaks down,
because `A⁻¹` does not exist.
