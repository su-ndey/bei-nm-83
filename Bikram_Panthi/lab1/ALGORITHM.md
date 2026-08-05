# Lab 1 - Bracketing Methods - Algorithms

Equation used: `f(x) = x³ - x - 2`, initial interval `[a, b] = [1, 2]`,
tolerance `ε = 0.0001`, maximum iterations = 100.

---

## 1. Bisection Method

### Algorithm

1. Start.
2. Define the function `f(x)`.
3. Input the initial guesses `a`, `b`, the tolerance `ε` and the maximum number of
   iterations.
4. Check whether `f(a) × f(b) < 0`. If it is not, display "Invalid interval" and
   stop, because the interval does not bracket a root.
5. Compute the midpoint `c = (a + b) / 2`.
6. If `f(c) = 0`, then `c` is the exact root; display it and stop.
7. Else if `f(a) × f(c) < 0`, the root lies in the left half, so set `b = c`.
8. Else the root lies in the right half, so set `a = c`.
9. If `|b - a| < ε`, display `c` as the approximate root and stop.
10. Otherwise repeat from step 5 until the maximum number of iterations is reached.
11. Stop.

### Pseudocode

```
BEGIN

Input a, b, tolerance, max_iter

IF f(a) * f(b) >= 0 THEN
    PRINT "Invalid interval"
    STOP
END IF

FOR i = 1 TO max_iter

    c = (a + b) / 2

    IF f(c) == 0 THEN
        PRINT "Exact root =", c
        STOP
    END IF

    IF f(a) * f(c) < 0 THEN
        b = c
    ELSE
        a = c
    END IF

    IF abs(b - a) < tolerance THEN
        PRINT "Approximate root =", c
        STOP
    END IF

END FOR

END
```

---

## 2. False Position Method (Regula-Falsi)

### Algorithm

1. Start.
2. Define the function `f(x)`.
3. Input `a`, `b`, the tolerance `ε` and the maximum number of iterations.
4. Check whether `f(a) × f(b) < 0`. If not, display "Invalid interval" and stop.
5. Compute the point where the straight line through `(a, f(a))` and `(b, f(b))`
   crosses the x-axis:

   ```
   c = ( a·f(b) - b·f(a) ) / ( f(b) - f(a) )
   ```

6. If `f(c) = 0`, then `c` is the exact root; display it and stop.
7. If `|c - c_previous| < ε`, display `c` as the approximate root and stop.
8. Else if `f(a) × f(c) < 0`, set `b = c`; otherwise set `a = c`.
9. Store `c` as `c_previous` and repeat from step 5.
10. Stop.

### Pseudocode

```
BEGIN

Input a, b, tolerance, max_iter

IF f(a) * f(b) >= 0 THEN
    PRINT "Invalid interval"
    STOP
END IF

c_old = a

FOR i = 1 TO max_iter

    c = (a*f(b) - b*f(a)) / (f(b) - f(a))

    IF f(c) == 0 THEN
        PRINT "Exact root =", c
        STOP
    END IF

    IF abs(c - c_old) < tolerance THEN
        PRINT "Approximate root =", c
        STOP
    END IF

    IF f(a) * f(c) < 0 THEN
        b = c
    ELSE
        a = c
    END IF

    c_old = c

END FOR

END
```

### Note on step 7

In this method one endpoint of the interval usually stays fixed, so `|b - a|` never
becomes small. I therefore test the change in `c` between successive iterations
instead of the width of the interval.
