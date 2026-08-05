# Lab 1 - Bracketing Methods

## Objective

To find the root of a nonlinear equation `f(x) = 0` using the Bisection Method and
the False Position Method, and to compare how quickly each one converges.

## Theory

Bracketing methods keep the root trapped inside an interval `[a, b]` where
`f(a) * f(b) < 0`. By the Intermediate Value Theorem the function must cross zero
somewhere inside that interval.

The equation I solved is `f(x) = x^3 - x - 2` on the interval `[1, 2]`.

- Bisection: `c = (a + b) / 2`
- False Position: `c = (a*f(b) - b*f(a)) / (f(b) - f(a))`

In both methods, if `f(a)*f(c) < 0` the root lies in `[a, c]` so I set `b = c`;
otherwise I set `a = c`.

## Programs

| File | Method |
|---|---|
| `bisection_method.py` | Bisection Method |
| `false_position_method.py` | False Position (Regula-Falsi) Method |

## Requirements

None - both programs use only the Python standard library.

## How to run

```bash
python bisection_method.py
python false_position_method.py
```

## Output

```
Bisection      -> Approximate root: 1.52142333984375   (14 iterations)
False Position -> Approximate root: 1.521344484231523  (8 iterations)
```

## Note on my implementation

For the False Position Method I used `|c_new - c_old| < tolerance` as the stopping
condition instead of `|b - a| < tolerance`. In this method one endpoint of the
interval usually stays fixed, so `|b - a|` never becomes small and the loop would
run to the maximum iteration count without ever reporting a root.

## Documents in this folder

| File | Contents |
|---|---|
| `README.md` | This file - objective, theory, results and discussion |
| `ALGORITHM.md` | Step-by-step algorithm and pseudocode for each method |
| `OUTPUT.md` | Full console output of every program |
| `*.py` | The Python programs |

## Discussion

- The Bisection Method always converges, but slowly, because the interval only
  halves each step.
- The False Position Method uses linear interpolation between the two endpoints and
  reached the same accuracy in 8 iterations instead of 14.
- Neither method can find complex roots, and both need a starting interval that
  actually brackets a root.

## Conclusion

I implemented both bracketing methods in Python and found the root of
`x^3 - x - 2 = 0` to be approximately **1.5214**. The Bisection Method was simpler
and completely reliable, while the False Position Method converged noticeably faster.
