# Lab 2 - Open Methods - Algorithms

Equation used: `f(x) = x³ - x - 2`, derivative `f'(x) = 3x² - 1`,
tolerance `ε = 0.0001`, maximum iterations = 100.

---

## 1. Secant Method

Initial guesses: `x0 = 1`, `x1 = 2`.

### Algorithm

1. Start.
2. Define the function `f(x)`.
3. Input the initial guesses `x0`, `x1`, the tolerance `ε` and the maximum number of
   iterations.
4. Check that `f(x1) - f(x0) ≠ 0`. If it is zero, display "Division by zero" and stop.
5. Compute the next approximation:

   ```
   x2 = x1 - f(x1)·(x1 - x0) / ( f(x1) - f(x0) )
   ```

6. If `|x2 - x1| < ε`, display `x2` as the approximate root and stop.
7. Otherwise update `x0 = x1` and `x1 = x2`.
8. Repeat from step 4 until convergence or until the maximum iterations are reached.
9. Plot the graph of `f(x)` to visualise the root.
10. Stop.

### Pseudocode

```
BEGIN

Input x0, x1, tolerance, max_iter

FOR i = 1 TO max_iter

    denominator = f(x1) - f(x0)

    IF denominator == 0 THEN
        PRINT "Division by zero encountered"
        STOP
    END IF

    x2 = x1 - (f(x1)*(x1 - x0)) / denominator

    IF abs(x2 - x1) < tolerance THEN
        PRINT "Approximate root =", x2
        STOP
    END IF

    x0 = x1
    x1 = x2

END FOR

END
```

---

## 2. Newton-Raphson Method

Initial guess: `x0 = 1.5`.

### Algorithm

1. Start.
2. Define the function `f(x)` and its derivative `f'(x)`.
3. Input the initial guess `x0`, the tolerance `ε` and the maximum number of
   iterations.
4. Check that `f'(x0) ≠ 0`. If it is zero, display "Derivative became zero" and stop.
5. Compute the next approximation using the tangent at the current point:

   ```
   x1 = x0 - f(x0) / f'(x0)
   ```

6. If `|x1 - x0| < ε`, display `x1` as the approximate root and stop.
7. Otherwise set `x0 = x1`.
8. Repeat from step 4 until convergence or until the maximum iterations are reached.
9. Plot the graph of `f(x)` to visualise the root.
10. Stop.

### Pseudocode

```
BEGIN

Input x0, tolerance, max_iter

FOR i = 1 TO max_iter

    derivative = f'(x0)

    IF derivative == 0 THEN
        PRINT "Derivative became zero"
        STOP
    END IF

    x1 = x0 - f(x0)/derivative

    IF abs(x1 - x0) < tolerance THEN
        PRINT "Approximate root =", x1
        STOP
    END IF

    x0 = x1

END FOR

END
```
