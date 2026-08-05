# Lab 6 - Curve Fitting and Interpolation - Algorithms

---

## Task 1: Exponential Curve Fitting by Least Squares

**Objective:** find the best-fit curve `y = A·e^(Bx)` for a set of data points.

**Theory.** Taking natural logarithms of both sides linearises the curve:

```
ln y = ln A + Bx
```

Writing `Y = ln y` and `a = ln A` gives the straight line `Y = a + Bx`, so the
ordinary least-squares formulas apply:

```
B = ( n·Σxy - Σx·Σy ) / ( n·Σx² - (Σx)² )
a = ( Σy - B·Σx ) / n
A = e^a
```

### Algorithm

1. Start.
2. Input the number of data points `n` and the points `(x_i, y_i)`.
3. Initialise the sums `Σx = 0`, `ΣY = 0`, `Σx² = 0`, `ΣxY = 0`.
4. For each data point `(x_i, y_i)`:
   a. Compute `Y_i = ln(y_i)`.
   b. Accumulate `Σx += x_i`, `ΣY += Y_i`, `Σx² += x_i²`, `ΣxY += x_i·Y_i`.
5. Compute `B = ( n·ΣxY - Σx·ΣY ) / ( n·Σx² - (Σx)² )`.
6. Compute `a = ( ΣY - B·Σx ) / n` and then `A = e^a`.
7. Display the fitted curve `y = A·e^(Bx)`.
8. Stop.

### Pseudocode

```
BEGIN

Input n and the data points (x, y)

sum_x = 0, sum_Y = 0, sum_x2 = 0, sum_xY = 0

FOR i = 1 TO n
    Y = ln(y[i])
    sum_x  += x[i]
    sum_Y  += Y
    sum_x2 += x[i] * x[i]
    sum_xY += x[i] * Y
END FOR

B = (n*sum_xY - sum_x*sum_Y) / (n*sum_x2 - sum_x^2)
a = (sum_Y - B*sum_x) / n
A = exp(a)

PRINT "y =", A, "* e^(", B, "x )"

END
```

**Condition:** every `y` value must be strictly positive, since `ln y` is otherwise
undefined.

---

## Task 2: Lagrange Interpolation

**Objective:** estimate the value of a function at a point lying between known data
points.

**Theory.** For `n` data points the interpolating polynomial is:

```
P(x) = Σ y_i · L_i(x)      where     L_i(x) = Π (x - x_j) / (x_i - x_j)   for j ≠ i
```

Each basis polynomial `L_i(x)` equals 1 at `x_i` and 0 at every other data point, so
the sum passes exactly through all the given points.

### Algorithm

1. Start.
2. Input the number of data points `n`, the points `(x_i, y_i)` and the value
   `x_val` at which the function is to be estimated.
3. Initialise `sum = 0`.
4. For each `i` from 0 to `n-1`:
   a. Initialise `term = y_i`.
   b. For each `j ≠ i`, multiply `term` by `(x_val - x_j) / (x_i - x_j)`.
   c. Add `term` to `sum`.
5. Output `sum` as the interpolated value `f(x_val)`.
6. Stop.

### Pseudocode

```
BEGIN

Input n, the data points (x, y), and x_val

result = 0

FOR i = 0 TO n-1

    term = y[i]

    FOR j = 0 TO n-1
        IF j != i THEN
            term = term * (x_val - x[j]) / (x[i] - x[j])
        END IF
    END FOR

    result = result + term

END FOR

PRINT "Interpolated value =", result

END
```

**Condition:** all `x` values must be distinct, otherwise `x_i - x_j` becomes zero.
