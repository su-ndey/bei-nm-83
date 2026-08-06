# Lab 4 (Part I) - LU Factorization - Algorithms

Both methods decompose `A = L·U` and then solve the system in two stages:

```
L Y = B     by forward substitution
U X = Y     by backward substitution
```

**Forward substitution**  `Y[i] = ( B[i] - Σ L[i][j]·Y[j] ) / L[i][i]`  for `j < i`

**Backward substitution** `X[i] = ( Y[i] - Σ U[i][j]·X[j] ) / U[i][i]`  for `j > i`

(When a diagonal is fixed at 1 the division by it can be omitted.)

---

## 1. Doolittle Method

The diagonal of `L` is fixed at 1:

```
      | 1    0    0 |
L =   | l21  1    0 |
      | l31  l32  1 |
```

**Formulas**

```
u(i,j) = a(i,j) - Σ l(i,k)·u(k,j)                     for k = 1 .. i-1
l(i,j) = ( a(i,j) - Σ l(i,k)·u(k,j) ) / u(j,j)        for k = 1 .. j-1
```

### Algorithm

1. Start.
2. Input the matrix `A` and the vector `B`.
3. Initialise `L` as the identity matrix and `U` as a zero matrix.
4. For each row `i` from 0 to `n-1`:
   a. For each column `j` from `i` to `n-1`, compute the upper triangular entry
      `U[i][j] = A[i][j] - Σ L[i][k]·U[k][j]` for `k < i`.
   b. For each row `j` from `i+1` to `n-1`, compute the lower triangular entry
      `L[j][i] = ( A[j][i] - Σ L[j][k]·U[k][i] ) / U[i][i]` for `k < i`.
5. Display the matrices `L` and `U`.
6. Solve `L Y = B` by forward substitution. Since the diagonal of `L` is 1,
   `Y[i] = B[i] - Σ L[i][j]·Y[j]`.
7. Solve `U X = Y` by backward substitution.
8. Display the solution `X`.
9. Stop.

### Pseudocode

```
BEGIN

Initialize L = identity, U = zeros

FOR each row i
    Compute the U entries of row i
    Compute the L entries of column i
END FOR

Solve L Y = B      (forward substitution)
Solve U X = Y      (backward substitution)

END
```

---

## 2. Crout's Method

The diagonal of `U` is fixed at 1:

```
      | 1  u12  u13 |
U =   | 0   1   u23 |
      | 0   0    1  |
```

**Formulas**

```
l(i,j) = a(i,j) - Σ l(i,k)·u(k,j)                     for k = 1 .. j-1
u(i,j) = ( a(i,j) - Σ l(i,k)·u(k,j) ) / l(i,i)        for k = 1 .. i-1
```

### Algorithm

1. Start.
2. Input the matrix `A` and the vector `B`.
3. Initialise `L` as a zero matrix and `U` as the identity matrix.
4. For each column `j` from 0 to `n-1`:
   a. For each row `i` from `j` to `n-1`, compute the lower triangular entry
      `L[i][j] = A[i][j] - Σ L[i][k]·U[k][j]` for `k < j`.
   b. For each column `i` from `j+1` to `n-1`, compute the upper triangular entry
      `U[j][i] = ( A[j][i] - Σ L[j][k]·U[k][i] ) / L[j][j]` for `k < j`.
5. Display the matrices `L` and `U`.
6. Solve `L Y = B` by forward substitution.
7. Solve `U X = Y` by backward substitution. Since the diagonal of `U` is 1,
   `X[i] = Y[i] - Σ U[i][j]·X[j]`.
8. Display the solution `X`.
9. Stop.

### Pseudocode

```
BEGIN

Initialize L = zeros, U = identity

FOR each column j
    Compute the L entries of column j
    Compute the U entries of row j
END FOR

Solve L Y = B      (forward substitution)
Solve U X = Y      (backward substitution)

END
```
