# Lab 6 - Curve Fitting and Interpolation

## Objective

To fit the best exponential curve to a set of data points using the method of least
squares, and to estimate the value of a function at an intermediate point using
Lagrange Interpolation.

## Programs

| File | Task |
|---|---|
| `exponential_curve_fitting.py` | Task 1 - least-squares fit of `y = A·e^(Bx)` |
| `lagrange_interpolation.py` | Task 2 - Lagrange Interpolation |

## Task 1: Exponential Curve Fitting

Taking the natural logarithm of `y = A·e^(Bx)` turns the curve into a straight line:

```
ln y = ln A + Bx      ->      Y = a + Bx      (where Y = ln y and a = ln A)
```

so the ordinary linear least-squares formulas apply:

```
B = ( n·Σxy - Σx·Σy ) / ( n·Σx² - (Σx)² )
a = ( Σy - B·Σx ) / n
A = e^a
```

With the sample data in my program (`x = 1, 2, 3, 4` and
`y = 1.65, 2.70, 4.50, 7.35`) the fitted curve is:

```
y = 1.0001 · e^(0.4993x)
```

My program also prints the fitted `y` value beside each given `y` value so the
quality of the fit can be seen at a glance. To fit a different data set, I only need
to change the `x_data` and `y_data` lists at the top of the file.

## Task 2: Lagrange Interpolation

```
P(x) = Σ y_i · L_i(x),      L_i(x) = Π (x - x_j)/(x_i - x_j)   for j ≠ i
```

With the data `x = [5, 7, 11, 13]` and `y = [150, 392, 1452, 2366]`, interpolating
at `x = 9`:

```
Interpolated value at x = 9 is 810.0000
```

## Requirements

None - only the standard `math` module is used.

## How to run

```bash
python exponential_curve_fitting.py
python lagrange_interpolation.py
```

## Note on my implementation

I put the data points in lists at the top of each file instead of reading them one
at a time with `input()`, so the programs run immediately in VS Code and the data
used is visible in the source. The formulas are unchanged.

## Documents in this folder

| File | Contents |
|---|---|
| `README.md` | This file - objective, theory, results and discussion |
| `ALGORITHM.md` | Step-by-step algorithm and pseudocode for each method |
| `OUTPUT.md` | Full console output of every program |
| `*.py` | The Python programs |

## Discussion

- The logarithmic transformation only works when every `y` value is strictly
  positive, since `ln y` is undefined otherwise.
- Least squares minimises the error in the transformed variable `Y = ln y`, not in
  `y` itself, so it slightly favours the smaller data values.
- Lagrange Interpolation is convenient for a small number of points and needs no
  equally spaced data, but it becomes expensive and can oscillate badly (Runge's
  phenomenon) when the number of points is large.

## Conclusion

I implemented exponential curve fitting by least squares and Lagrange
Interpolation. The first let me fit a smooth exponential trend through scattered
data, and the second let me estimate a function value between known data points.
