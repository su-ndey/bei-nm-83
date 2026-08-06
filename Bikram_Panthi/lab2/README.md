# Lab 2 - Open Methods

## Objective

To find the roots of a nonlinear equation using the Secant Method and the
Newton-Raphson Method, to study how open methods converge, and to visualise the
equation using Matplotlib.

## Theory

Open methods do not need the root to be bracketed. They start from initial guesses
and iterate towards the root, which makes them faster but also means they can
diverge if the starting values are poor.

The equation I solved is `f(x) = x^3 - x - 2`, with `f'(x) = 3x^2 - 1`.

- Secant: `x(n+1) = x(n) - f(x(n)) * (x(n) - x(n-1)) / (f(x(n)) - f(x(n-1)))`
- Newton-Raphson: `x(n+1) = x(n) - f(x(n)) / f'(x(n))`

## Programs

| File | Method |
|---|---|
| `secant_method.py` | Secant Method, with a graph of `f(x)` |
| `newton_raphson_method.py` | Newton-Raphson Method, with a graph of `f(x)` |

## Requirements

None for the calculation itself. I built the list of plotting points with a list
comprehension rather than `numpy.linspace`, so the programs run on a plain Python
installation.

`matplotlib` is optional: if it is installed the program shows the graph after
printing the iterations, and if it is not installed the program prints a short
notice and finishes normally. To see the graph:

```bash
pip install matplotlib
```

## How to run

```bash
python secant_method.py
python newton_raphson_method.py
```

If the plot window opens, close it to end the program.

## Output

Both methods converge to the same root, `x ≈ 1.5214`. Newton-Raphson reaches it in
the fewest iterations of all four methods from Labs 1 and 2.

## Documents in this folder

| File | Contents |
|---|---|
| `README.md` | This file - objective, theory, results and discussion |
| `ALGORITHM.md` | Step-by-step algorithm and pseudocode for each method |
| `OUTPUT.md` | Full console output of every program |
| `*.py` | The Python programs |

## Discussion

- Newton-Raphson converges fastest because it uses the exact derivative, but it
  fails wherever `f'(x) = 0`. My program checks for this before dividing.
- The Secant Method avoids the derivative by approximating it from the last two
  points, which is useful when the derivative is hard to write down. It breaks down
  if `f(x1) == f(x0)`, so I check the denominator before dividing.
- The graph makes it easy to see roughly where the root lies before choosing the
  initial guesses.

## Conclusion

I implemented both open methods in Python. Both located the root of
`x^3 - x - 2 = 0` successfully, with Newton-Raphson converging fastest because it
uses derivative information, while the Secant Method avoided calculating the
derivative altogether.
