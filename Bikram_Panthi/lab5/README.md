# Lab 5 - Gauss-Jordan, Power Method and Inverse Power Method

## Objective

To solve a system of linear equations by the direct Gauss-Jordan Elimination
Method, to find the dominant eigenvalue and eigenvector using the Power Method, and
to find the smallest eigenvalue using the Inverse Power Method.

## Programs

| File | Method | Finds |
|---|---|---|
| `gauss_jordan.py` | Gauss-Jordan Elimination | the solution of `AX = B` |
| `power_method.py` | Power Method | the largest eigenvalue and its eigenvector |
| `inverse_power_method.py` | Inverse Power Method | the smallest eigenvalue and its eigenvector |

## 1. Gauss-Jordan Elimination

Instead of stopping at an upper triangular matrix, Gauss-Jordan clears the entries
both below **and** above every pivot, reducing the augmented matrix all the way to
the identity:

```
[A | B]  --(elementary row operations)-->  [I | X]
```

so the solution is read off directly with no back substitution.

System solved:

```
 2x +  y -  z =   8
-3x -  y + 2z = -11
-2x +  y + 2z =  -3
```

Result: `x = 2, y = 3, z = -1`. My program also prints the reduced matrix so the
identity can be seen.

## 2. Power Method

Starting from a nonzero guess vector, I repeatedly compute `Y = A * X` and normalise
by the component of largest magnitude. That scaling factor converges to the dominant
eigenvalue and the vector converges to its eigenvector.

Matrix used:

```
[ 4  1  0 ]
[ 1 20  1 ]
[ 0  1  4 ]
```

Result: `Dominant Eigenvalue = 20.12404`, eigenvector `[0.062019, 1.0, 0.062019]`.

As a check, my program also prints the Rayleigh quotient `(XᵀAX)/(XᵀX)`, which gives
the same value of 20.12404.

## 3. Inverse Power Method

If `A` has eigenvalue `λ`, then `A⁻¹` has eigenvalue `1/λ`. So applying the Power
Method to `A⁻¹` finds the *smallest* eigenvalue of `A`:

```
λ_smallest = 1 / λ_max(A⁻¹)
```

To avoid computing an explicit inverse, I solve the system `A * Y = X` at every
iteration instead.

Result: `Smallest Eigenvalue = 3.87596`.

The three true eigenvalues of this matrix are `20.1240, 4.0000, 3.8760`, so both
iterative methods picked out the correct extremes.

## Requirements

None - pure Python. Since the Inverse Power Method needs to solve `A * Y = X` each
iteration, I wrote a small `solve()` helper inside the file that does Gaussian
elimination with partial pivoting, reusing what I implemented in Lab 3.

## How to run

```bash
python gauss_jordan.py
python power_method.py
python inverse_power_method.py
```

## Documents in this folder

| File | Contents |
|---|---|
| `README.md` | This file - objective, theory, results and discussion |
| `ALGORITHM.md` | Step-by-step algorithm and pseudocode for each method |
| `OUTPUT.md` | Full console output of every program |
| `*.py` | The Python programs |

## Discussion

- Gauss-Jordan needs about 50% more arithmetic than Gaussian elimination with back
  substitution, but the same technique also produces the matrix inverse through
  `[A | I] -> [I | A⁻¹]`.
- Normalising the vector at every iteration is essential; without it the entries
  grow or shrink until they overflow or underflow.
- The Power Method fails if two eigenvalues share the largest magnitude with
  opposite signs, and converges slowly when the second largest eigenvalue is close
  to the dominant one.
- The initial guess vector must not be orthogonal to the eigenvector being sought.

## Conclusion

I implemented all three methods in Python. Gauss-Jordan gave the exact solution of
the system directly, while the Power and Inverse Power Methods found the largest and
smallest eigenvalues of the matrix. Together they cover the direct and the iterative
approaches to matrix computation.
