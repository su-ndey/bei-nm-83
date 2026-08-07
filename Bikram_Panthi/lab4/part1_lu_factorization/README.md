# Lab 4 - Part I: LU Factorization (Doolittle and Crout)

## Objective

To solve a system of linear equations by decomposing the coefficient matrix into a
lower triangular matrix `L` and an upper triangular matrix `U`, using both the
Doolittle and Crout methods.

## Theory

LU factorization writes `A = L * U`, which turns `AX = B` into two easy triangular
systems:

```
L Y = B     (solved by forward substitution)
U X = Y     (solved by backward substitution)
```

The difference between the two methods is which diagonal is fixed at 1:

| Method | Fixed diagonal |
|---|---|
| Doolittle | diagonal of **L** is 1 |
| Crout | diagonal of **U** is 1 |

Doolittle formulas:

```
u(i,j) = a(i,j) - Σ l(i,k)*u(k,j)                    for k < i
l(i,j) = ( a(i,j) - Σ l(i,k)*u(k,j) ) / u(j,j)
```

Crout formulas:

```
l(i,j) = a(i,j) - Σ l(i,k)*u(k,j)                    for k < j
u(i,j) = ( a(i,j) - Σ l(i,k)*u(k,j) ) / l(i,i)
```

## Programs

| File | Method |
|---|---|
| `doolittle_method.py` | Doolittle Method |
| `crout_method.py` | Crout's Method |

## System solved

```
 2x -  y - 2z = -2
-4x + 6y + 3z =  9
-4x - 2y + 8z = -5
```

Both programs print the `L` and `U` matrices and then the same solution:

```
x = -1.875,  y = 0.916667,  z = -1.333333
```

I checked this answer by substituting it back into all three original equations.

## Requirements

None - pure Python, no `pip install` needed.

## How to run

```bash
python doolittle_method.py
python crout_method.py
```

## Documents in this folder

| File | Contents |
|---|---|
| `README.md` | This file - objective, theory, results and discussion |
| `ALGORITHM.md` | Step-by-step algorithm and pseudocode for each method |
| `OUTPUT.md` | Full console output of every program |
| `*.py` | The Python programs |

## Discussion

- Both methods decompose the same matrix but distribute the values differently
  between `L` and `U`; the final solution is identical, which is a good check that
  both implementations are correct.
- LU factorization is most useful when several systems share the same matrix `A`:
  the decomposition is done once and reused with each new `B`, so only the cheap
  forward and backward substitutions are repeated.
- The method needs a non-singular matrix, and it breaks down if a pivot becomes
  zero, so pivoting may be required for some matrices.

## Conclusion

I implemented LU factorization by both the Doolittle and Crout methods. Both
decomposed the matrix successfully and produced the same solution, confirming that
LU decomposition is an efficient way to reduce a full system to two simple
triangular systems.
