# Lab 8 - Solution of Ordinary Differential Equations - Algorithms

## Reducing a second-order ODE to a system

A second-order equation `d²y/dx² = f(x, y, y')` is solved numerically by first
introducing `z = dy/dx`, which turns it into two coupled first-order equations:

```
dy/dx = z            call this  g(x, y, z)
dz/dx = f(x, y, z)   call this  h(x, y, z)
```

Both are then advanced together, one step at a time, using the same step size `h`.

Initial conditions used in both programs: `x0 = 0`, `y0 = 0`, `z0 = 10`, with step
size `h = 0.1` for 10 steps.

---

## 1. Runge-Kutta 2nd Order Method (RK2)

RK2 estimates the increment from the slope at the **midpoint** of the step, which is
more accurate than Euler's method's slope at the start of the step.

**Formulas**

```
k1 = h · g(x, y, z)
l1 = h · h_(x, y, z)

k2 = h · g( x + h/2,  y + k1/2,  z + l1/2 )
l2 = h · h_( x + h/2,  y + k1/2,  z + l1/2 )

y(n+1) = y(n) + k2
z(n+1) = z(n) + l2
x(n+1) = x(n) + h
```

**System solved:** `dy/dx = z`, `dz/dx = -10·sin(x)`

### Algorithm

1. Start.
2. Define the two functions `g(x, y, z)` and `h(x, y, z)`.
3. Initialise `x = x0`, `y = y0`, `z = z0`, and set the step size `h` and the number
   of steps.
4. For each step:
   a. Compute `k1` and `l1` using the slopes at the start of the interval.
   b. Compute `k2` and `l2` using the slopes at the midpoint, i.e. at
      `x + h/2`, `y + k1/2`, `z + l1/2`.
   c. Update `y = y + k2` and `z = z + l2`.
   d. Increment `x = x + h`.
5. Repeat for the required number of steps.
6. Display the final values of `y` and `dy/dx`.
7. Stop.

### Pseudocode

```
function g(x, y, z): return z
function h_(x, y, z): return -10 * sin(x)

initialize x, y, z, h, steps

FOR i = 1 TO steps
    k1 = h * g(x, y, z)
    l1 = h * h_(x, y, z)

    k2 = h * g(x + h/2, y + k1/2, z + l1/2)
    l2 = h * h_(x + h/2, y + k1/2, z + l1/2)

    y = y + k2
    z = z + l2
    x = x + h
END FOR

PRINT y, z
```

---

## 2. Runge-Kutta 4th Order Method (RK4)

RK4 samples four slopes across each step and combines them in a weighted average,
giving considerably higher accuracy for the same step size.

**Formulas**

```
k1 = h · g(x, y, z)
l1 = h · h_(x, y, z)

k2 = h · g( x + h/2,  y + k1/2,  z + l1/2 )
l2 = h · h_( x + h/2,  y + k1/2,  z + l1/2 )

k3 = h · g( x + h/2,  y + k2/2,  z + l2/2 )
l3 = h · h_( x + h/2,  y + k2/2,  z + l2/2 )

k4 = h · g( x + h,  y + k3,  z + l3 )
l4 = h · h_( x + h,  y + k3,  z + l3 )

y(n+1) = y(n) + ( k1 + 2k2 + 2k3 + k4 ) / 6
z(n+1) = z(n) + ( l1 + 2l2 + 2l3 + l4 ) / 6
x(n+1) = x(n) + h
```

**System solved:** `dy/dx = 12x² + y + z`, `dz/dx = -10·sin(x) + 2y + 3z`

### Algorithm

1. Start.
2. Define the two functions `g(x, y, z)` and `h(x, y, z)`.
3. Initialise `x = x0`, `y = y0`, `z = z0`, and set the step size `h` and the number
   of steps.
4. For each step:
   a. Compute `k1`, `l1` at the start of the interval.
   b. Compute `k2`, `l2` at the midpoint, using `k1` and `l1`.
   c. Compute `k3`, `l3` at the midpoint again, this time using `k2` and `l2`.
   d. Compute `k4`, `l4` at the end of the interval, using `k3` and `l3`.
   e. Update `y = y + (k1 + 2k2 + 2k3 + k4)/6` and
      `z = z + (l1 + 2l2 + 2l3 + l4)/6`.
   f. Increment `x = x + h`.
5. Repeat for the required number of steps.
6. Display the final values of `y` and `dy/dx`.
7. Stop.

### Pseudocode

```
function g(x, y, z): return 12*x^2 + y + z
function h_(x, y, z): return -10*sin(x) + 2*y + 3*z

initialize x, y, z, h, steps

FOR i = 1 TO steps
    k1 = h * g(x, y, z)
    l1 = h * h_(x, y, z)

    k2 = h * g(x + h/2, y + k1/2, z + l1/2)
    l2 = h * h_(x + h/2, y + k1/2, z + l1/2)

    k3 = h * g(x + h/2, y + k2/2, z + l2/2)
    l3 = h * h_(x + h/2, y + k2/2, z + l2/2)

    k4 = h * g(x + h, y + k3, z + l3)
    l4 = h * h_(x + h, y + k3, z + l3)

    y = y + (k1 + 2*k2 + 2*k3 + k4)/6
    z = z + (l1 + 2*l2 + 2*l3 + l4)/6
    x = x + h
END FOR

PRINT y, z
```

### Comparison

RK2 needs two slope evaluations per step and has a local truncation error of order
`h³`; RK4 needs four and has a local error of order `h⁵`. RK4 therefore gives much
better accuracy for the same step size, at roughly twice the computational cost per
step.
