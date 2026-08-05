# Lab 8 - Solution of Ordinary Differential Equations (RK2 and RK4)

## Objective

To solve second-order ordinary differential equations by converting them into
systems of first-order equations, and to apply the Runge-Kutta methods of 2nd order
(RK2) and 4th order (RK4).

## Theory

A second-order ODE of the form `d²y/dx² = f(x, y, y')` is reduced to two first-order
equations by defining `z = dy/dx`:

```
dy/dx = z
dz/dx = f(x, y, z)
```

Both equations are then advanced together, one step at a time.

**RK2** uses the slope at the midpoint of the step:

```
k1 = h·g(x, y, z)                         l1 = h·h_(x, y, z)
k2 = h·g(x + h/2, y + k1/2, z + l1/2)     l2 = h·h_(x + h/2, y + k1/2, z + l1/2)
y = y + k2      z = z + l2      x = x + h
```

**RK4** samples four slopes per step and takes a weighted average:

```
k1..k4 and l1..l4 evaluated at x, x + h/2, x + h/2 and x + h
y = y + (k1 + 2k2 + 2k3 + k4)/6
z = z + (l1 + 2l2 + 2l3 + l4)/6
x = x + h
```

## Programs

| File | Method | System solved |
|---|---|---|
| `rk2_method.py` | Runge-Kutta 2nd order | `dy/dx = z`, `dz/dx = -10 sin(x)` |
| `rk4_method.py` | Runge-Kutta 4th order | `dy/dx = 12x² + y + z`, `dz/dx = -10 sin(x) + 2y + 3z` |

Both use the initial conditions `x0 = 0, y0 = 0, z0 = 10` with step size `h = 0.1`
for 10 steps, so the solution is advanced from `x = 0` to `x = 1`.

## Output

```
RK2 ->  y(1.0) =   8.428357      dy/dx(1.0) =   5.401107
RK4 ->  y(1.0) = 117.145284      dy/dx(1.0) = 316.366039
```

The two answers are very different because the two problems are different systems,
not because of the methods. Both of my programs also print a step-by-step table of
`x`, `y` and `dy/dx` so the whole solution can be followed.

## Requirements

None - only the standard `math` module is used.

## How to run

```bash
python rk2_method.py
python rk4_method.py
```

## Documents in this folder

| File | Contents |
|---|---|
| `README.md` | This file - objective, theory, results and discussion |
| `ALGORITHM.md` | Step-by-step algorithm and pseudocode for each method |
| `OUTPUT.md` | Full console output of every program |
| `*.py` | The Python programs |

## Discussion

- RK2 improves on Euler's method by using the midpoint slope instead of the slope at
  the start of the interval; its local truncation error is of order `h³`.
- RK4 evaluates four slopes per step and has local error of order `h⁵`, which is why
  it is the standard choice in practice.
- Reducing `h` improves accuracy but multiplies the number of function evaluations,
  so there is a trade-off between accuracy and computation time.
- The same code structure handles any coupled first-order system - only the two
  functions `dy` and `dz` need changing.

## Conclusion

I implemented the RK2 and RK4 methods in Python and used them to solve second-order
ODEs after reducing them to systems of first-order equations. RK4 requires more
function evaluations per step but gives considerably better accuracy, making it the
more useful method for problems that cannot be solved analytically.
