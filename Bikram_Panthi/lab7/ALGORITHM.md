# Lab 7 - Numerical Integration - Algorithms

Function integrated: `f(x) = 1 / (1 + x³)`, from `x0 = 0` to `xn = 1` with `n = 6`
sub-intervals. In every rule the step size is:

```
h = ( xn - x0 ) / n
```

---

## Task 1: Trapezoidal Rule

Each sub-interval is approximated by a trapezium, i.e. the curve is replaced by a
straight line between consecutive points.

```
Area = (h/2) · [ f(x0) + f(xn) + 2·Σ f(interior points) ]
```

### Algorithm

1. Input the lower limit `x0`, the upper limit `xn` and the number of sub-intervals
   `n`.
2. Compute the step size `h = (xn - x0) / n`.
3. Compute `sum = f(x0) + f(xn)`.
4. For `i = 1` to `n-1`:
   - Compute `x = x0 + i·h`.
   - Add `2·f(x)` to `sum`.
5. Compute `Area = (h/2) · sum`.
6. Display the area.

### Pseudocode

```
Input x0, xn, n
h = (xn - x0) / n
sum = f(x0) + f(xn)

FOR i = 1 TO n-1
    x = x0 + i*h
    sum = sum + 2*f(x)
END FOR

Area = (h/2) * sum
PRINT Area
```

**Note:** the interior points carry a weight of 2 because the factor `h/2` sits
outside the bracket. Only the two end points carry a weight of 1.

---

## Task 2: Simpson's 1/3 Rule

Groups of three consecutive points are fitted with a parabola. The interior points
alternate in weight: odd-indexed points get 4, even-indexed points get 2.

```
Area = (h/3) · [ f(x0) + f(xn) + 4·Σ f(odd i) + 2·Σ f(even i) ]
```

### Algorithm

1. Input `x0`, `xn` and `n`, where **`n` must be even**.
2. Compute `h = (xn - x0) / n`.
3. Compute `sum = f(x0) + f(xn)`.
4. For `i = 1` to `n-1`:
   - Compute `x = x0 + i·h`.
   - If `i` is even, add `2·f(x)` to `sum`.
   - If `i` is odd, add `4·f(x)` to `sum`.
5. Compute `Area = (h/3) · sum`.
6. Display the area.

### Pseudocode

```
Input x0, xn, n            (n must be even)
h = (xn - x0) / n
sum = f(x0) + f(xn)

FOR i = 1 TO n-1
    x = x0 + i*h
    IF i mod 2 == 0 THEN
        sum = sum + 2*f(x)
    ELSE
        sum = sum + 4*f(x)
    END IF
END FOR

Area = (h/3) * sum
PRINT Area
```

---

## Task 3: Simpson's 3/8 Rule

Groups of four consecutive points are fitted with a cubic. Every third point gets a
weight of 2, and all the others get 3.

```
Area = (3h/8) · [ f(x0) + f(xn) + 2·Σ f(every 3rd i) + 3·Σ f(the rest) ]
```

### Algorithm

1. Input `x0`, `xn` and `n`, where **`n` must be divisible by 3**.
2. Compute `h = (xn - x0) / n`.
3. Compute `sum = f(x0) + f(xn)`.
4. For `i = 1` to `n-1`:
   - Compute `x = x0 + i·h`.
   - If `i mod 3 == 0`, add `2·f(x)` to `sum`.
   - Otherwise add `3·f(x)` to `sum`.
5. Compute `Area = (3h/8) · sum`.
6. Display the area.

### Pseudocode

```
Input x0, xn, n            (n must be divisible by 3)
h = (xn - x0) / n
sum = f(x0) + f(xn)

FOR i = 1 TO n-1
    x = x0 + i*h
    IF i mod 3 == 0 THEN
        sum = sum + 2*f(x)
    ELSE
        sum = sum + 3*f(x)
    END IF
END FOR

Area = (3*h/8) * sum
PRINT Area
```
