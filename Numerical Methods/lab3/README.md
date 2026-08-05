# Lab 3 - Gaussian Elimination with Pivoting

## Objective

To solve systems of linear equations using Gaussian Elimination with Partial
Pivoting and with Complete Pivoting, and to understand how pivoting improves
numerical stability.

## Theory

Gaussian Elimination converts the coefficient matrix of `AX = B` into upper
triangular form using elementary row operations, then finds the unknowns by back
substitution:

```
xn = bn / ann          and          xi = ( bi - Σ aij*xj ) / aii
```

Pivoting rearranges the matrix so that the number I divide by is as large as
possible, which avoids dividing by very small numbers and reduces round-off error.

- **Partial pivoting** picks the largest absolute element in the current column and
  swaps rows only.
- **Complete pivoting** picks the largest absolute element in the entire remaining
  submatrix and swaps both rows and columns. Because columns move, the order of the
  variables changes and has to be restored at the end.

## Programs

| File | Method |
|---|---|
| `gauss_elimination_partial_pivoting.py` | Partial pivoting (row swaps only) |
| `gauss_elimination_complete_pivoting.py` | Complete pivoting (row and column swaps) |

I represented the matrices as nested lists, following the "Prerequisite Python
Concepts" section of the lab sheet.

## Systems solved and results

**Partial pivoting**

```
 2x +  y -  z =   8
-3x -  y + 2z = -11
-2x +  y + 2z =  -3
```

Result: `x = 2, y = 3, z = -1` (I verified this by substituting back into all three
equations.)

**Complete pivoting**

```
      2y +  z =   8
 x - 2y - 3z = -11
2x + 3y +  z =  -3
```

Result: `x = -8.142857, y = 5.285714, z = -2.571429`

Note that the first coefficient of this system is 0, so without pivoting the very
first step would divide by zero. This is exactly the situation pivoting exists for.

## Requirements

None - written in pure Python using nested lists, so no `pip install` is needed.

## How to run

```bash
python gauss_elimination_partial_pivoting.py
python gauss_elimination_complete_pivoting.py
```

## Note on my implementation

In the complete pivoting program I kept a `col_index` list to record every column
swap, and used it at the end to put the solution values back against the correct
variables. Without this final rearrangement the answers come out attached to the
wrong unknowns.

## Documents in this folder

| File | Contents |
|---|---|
| `README.md` | This file - objective, theory, results and discussion |
| `ALGORITHM.md` | Step-by-step algorithm and pseudocode for each method |
| `OUTPUT.md` | Full console output of every program |
| `*.py` | The Python programs |

## Discussion

- Partial pivoting is cheap and sufficient for most systems.
- Complete pivoting is more stable but costs more, since it searches the whole
  remaining submatrix at each step and needs the variable order to be tracked.
- Round-off error can still build up in long eliminations, so pivoting reduces the
  problem rather than removing it entirely.

## Conclusion

I implemented Gaussian Elimination with both partial and complete pivoting in
Python. Both solved their systems correctly, and the exercise showed clearly why
pivoting is necessary - the complete pivoting system has a zero in the first pivot
position and cannot be solved without it.
