# Numerical Methods - Lab Work

**Submitted by:** Bikram Panthi (HCE081BEI013)
**Subject:** Numerical Methods (2nd Year, Engineering)
**Language:** Python 3

This repository contains my lab work for the Numerical Methods course. Each lab has
its own folder containing:

| File | Contents |
|---|---|
| `README.md` | Objective, theory, results, discussion and conclusion |
| `ALGORITHM.md` | The step-by-step algorithm and pseudocode for each method |
| `OUTPUT.md` | The complete console output of every program in that lab |
| `*.py` | The Python programs |

## Contents

| Lab | Topic | Programs |
|---|---|---|
| [lab1](lab1) | Bracketing Methods | Bisection, False Position |
| [lab2](lab2) | Open Methods | Secant, Newton-Raphson (with graph) |
| [lab3](lab3) | Gaussian Elimination with Pivoting | Partial pivoting, Complete pivoting |
| [lab4/part1](lab4/part1_lu_factorization) | LU Factorization | Doolittle, Crout |
| [lab4/part2](lab4/part2_iterative_methods) | Iterative Methods | Gauss-Jacobi, Gauss-Seidel |
| [lab5](lab5) | Direct Solution and Eigenvalues | Gauss-Jordan, Power, Inverse Power |
| [lab6](lab6) | Curve Fitting and Interpolation | Exponential least squares, Lagrange |
| [lab7](lab7) | Numerical Integration | Trapezoidal, Simpson 1/3, Simpson 3/8 |
| [lab8](lab8) | Ordinary Differential Equations | RK2, RK4 |

Lab 4 was given as two separate documents, so I have split that folder into
`part1_lu_factorization` and `part2_iterative_methods`.

## How to run

Every program runs on a plain Python 3 installation - there is nothing to install
and no virtual environment to set up. All matrices are ordinary nested lists, as
taught in the "Prerequisite Python Concepts" sections of the lab sheets.

Open the folder in VS Code and press Run on any file, or from a terminal:

```bash
cd lab1
python bisection_method.py
```

Each program has its input values - matrices, limits, initial guesses and
tolerances - written as plain variables at the top rather than read with `input()`.
This way the file runs and prints its result immediately, and the data used is
visible in the source. To solve a different problem I only need to edit those
variables.

The one optional extra is `matplotlib`, used by Lab 2 to draw a graph of the
nonlinear equation. If it is not installed the program still prints all its
iterations and the root, and simply skips the graph. To enable it:

```bash
pip install matplotlib
```

## Summary of results

| Lab | Result |
|---|---|
| 1 | root of `x³ - x - 2` ≈ 1.5214 (Bisection 14 iterations, False Position 8) |
| 2 | same root; Newton-Raphson converged in the fewest steps |
| 3 | `[2, 3, -1]` with partial pivoting; `[-8.142857, 5.285714, -2.571429]` with complete pivoting |
| 4 part 1 | `[-1.875, 0.916667, -1.333333]` from both Doolittle and Crout |
| 4 part 2 | `[1, 1, 1]`; Gauss-Jacobi 13 iterations, Gauss-Seidel 6 |
| 5 | `[2, 3, -1]`; λmax = 20.12404, λmin = 3.87596 |
| 6 | `y = 1.0001·e^(0.4993x)`; interpolated value 810.0 at x = 9 |
| 7 | ∫₀¹ dx/(1+x³): 0.8339 (Trapezoidal), 0.8357 (both Simpson) against a true value of 0.835649 |
| 8 | RK2: y(1) = 8.428357; RK4: y(1) = 117.145284 |

I ran every program and checked its output; the complete console output of each one
is recorded in the `OUTPUT.md` file of its lab folder. For the systems of equations I
verified the answers by substituting them back into the original equations, and for
the integration I compared my results against the true value of the integral.

## Notes on my implementations

A few places where I had to think carefully about the method, each explained in the
relevant lab README and in a comment in the code:

1. **Lab 1, False Position:** I used `|c_new - c_old| < tolerance` as the stopping
   condition, because one endpoint of the interval stays fixed in this method and
   `|b - a|` never becomes small.
2. **Lab 3, Complete Pivoting:** since columns are swapped as well as rows, I track
   the swaps in `col_index` and use it to restore the original variable order before
   printing the solution.
3. **Lab 4 Part I:** I verified my solution by substituting it back into the three
   equations. The values `x = 1, y = 2, z = -1` give `[2, 5, -16]` rather than
   `[-2, 9, -5]`, so they do not satisfy this particular system.
4. **Lab 4 Part II, Gauss-Jacobi:** I update `x_old` before testing for convergence,
   so the vector printed at the end is the converged one.
5. **Lab 7, Trapezoidal Rule:** the interior points carry a weight of 2, since the
   `h/2` factor is outside the bracket.

## Folder structure

```
Numerical Methods/
├── .gitignore
├── README.md
├── lab1/   README.md, ALGORITHM.md, OUTPUT.md
│           bisection_method.py, false_position_method.py
├── lab2/   README.md, ALGORITHM.md, OUTPUT.md
│           secant_method.py, newton_raphson_method.py
├── lab3/   README.md, ALGORITHM.md, OUTPUT.md
│           gauss_elimination_partial_pivoting.py,
│           gauss_elimination_complete_pivoting.py
├── lab4/   README.md
│   ├── part1_lu_factorization/   README.md, ALGORITHM.md, OUTPUT.md
│   │                             doolittle_method.py, crout_method.py
│   └── part2_iterative_methods/  README.md, ALGORITHM.md, OUTPUT.md
│                                 gauss_jacobi.py, gauss_seidel.py
├── lab5/   README.md, ALGORITHM.md, OUTPUT.md
│           gauss_jordan.py, power_method.py, inverse_power_method.py
├── lab6/   README.md, ALGORITHM.md, OUTPUT.md
│           exponential_curve_fitting.py, lagrange_interpolation.py
├── lab7/   README.md, ALGORITHM.md, OUTPUT.md
│           trapezoidal_rule.py, simpson_one_third_rule.py,
│           simpson_three_eighth_rule.py
└── lab8/   README.md, ALGORITHM.md, OUTPUT.md
            rk2_method.py, rk4_method.py
```

The `.gitignore` excludes `__pycache__`, virtual environments, editor settings and
other generated files, so only my source code and documentation are tracked.
