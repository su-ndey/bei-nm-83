# Lab 4 - Part II: Gauss-Jacobi and Gauss-Seidel

## Objective

To solve a system of linear equations using the iterative Gauss-Jacobi and
Gauss-Seidel methods, to verify the condition of Strict Diagonal Dominance, and to
compare the convergence speed of the two methods.

## Theory

Unlike direct methods, iterative methods start from a guess (I used all zeros) and
improve it step by step. They are efficient for large, sparse systems.

**Strict Diagonal Dominance (SDD)** guarantees convergence:

```
|a(i,i)| > Σ |a(i,j)| for all j ≠ i, in every row
```

Both of my programs check this condition before starting and print a warning if any
row fails it.

**Gauss-Jacobi** (simultaneous displacement) - a whole sweep uses only values from
the previous iteration:

```
x_i(k+1) = ( b_i - Σ_{j≠i} a(i,j) * x_j(k) ) / a(i,i)
```

**Gauss-Seidel** (successive displacement) - uses each new value as soon as it is
available, within the same sweep:

```
x_i(k+1) = ( b_i - Σ_{j<i} a(i,j)*x_j(k+1) - Σ_{j>i} a(i,j)*x_j(k) ) / a(i,i)
```

## Programs

| File | Method |
|---|---|
| `gauss_jacobi.py` | Gauss-Jacobi Method |
| `gauss_seidel.py` | Gauss-Seidel Method |

## System solved

```
10x +   y +  2z = 13
 2x + 10y +  3z = 15
  x +  2y + 10z = 13
```

This matrix is strictly diagonally dominant (10 > 1+2, 10 > 2+3, 10 > 1+2), so both
methods are guaranteed to converge. The solution is `x = y = z = 1`.

## Output

```
Gauss-Jacobi  -> converged in 13 iterations  (tolerance 1e-5)
Gauss-Seidel  -> converged in  6 iterations  (tolerance 1e-5)
```

Gauss-Seidel needed roughly half as many iterations, which matches the theory that
it converges about twice as fast.

## Requirements

None - pure Python, no `pip install` needed.

## How to run

```bash
python gauss_jacobi.py
python gauss_seidel.py
```

Both programs print every iteration together with its maximum absolute error.

## Note on my implementation

In the Jacobi program I copy `x_new` into `x_old` *before* checking the convergence
condition, so that the vector printed at the end is the converged one and not the
previous iteration's values.

## Documents in this folder

| File | Contents |
|---|---|
| `README.md` | This file - objective, theory, results and discussion |
| `ALGORITHM.md` | Step-by-step algorithm and pseudocode for each method |
| `OUTPUT.md` | Full console output of every program |
| `*.py` | The Python programs |

## Discussion

- Gauss-Jacobi computes each component independently of the others in the same
  sweep, which makes it well suited to parallel processing.
- Gauss-Seidel is faster in sequence because it immediately uses updated values, but
  that same dependency makes it hard to parallelise.
- If a system is not diagonally dominant, the rows can often be reordered until it
  is, before starting the iterations.

## Conclusion

I implemented both iterative methods and solved a strictly diagonally dominant
system with each. Both converged to `x = y = z = 1`, with Gauss-Seidel taking 6
iterations against Gauss-Jacobi's 13, confirming its faster convergence.
