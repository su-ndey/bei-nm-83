# Lab 7 - Numerical Integration

## Objective

To evaluate a definite integral numerically using the Trapezoidal Rule, Simpson's
1/3 Rule and Simpson's 3/8 Rule, and to compare their accuracy.

## Theory

The function I integrated is:

```
f(x) = 1 / (1 + x³)
```

Each rule replaces the curve with simple shapes over each sub-interval, with
`h = (xn - x0) / n`:

```
Trapezoidal:   Area = (h/2)  · [ f(x0) + f(xn) + 2·Σ f(interior) ]
Simpson 1/3:   Area = (h/3)  · [ f(x0) + f(xn) + 4·Σ f(odd) + 2·Σ f(even) ]
Simpson 3/8:   Area = (3h/8) · [ f(x0) + f(xn) + 2·Σ f(every 3rd) + 3·Σ f(rest) ]
```

The Trapezoidal Rule joins the points with straight lines, Simpson's 1/3 fits
parabolas through groups of three points, and Simpson's 3/8 fits cubics through
groups of four.

## Programs

| File | Rule | Restriction on n |
|---|---|---|
| `trapezoidal_rule.py` | Trapezoidal Rule | none |
| `simpson_one_third_rule.py` | Simpson's 1/3 Rule | `n` must be even |
| `simpson_three_eighth_rule.py` | Simpson's 3/8 Rule | `n` must be divisible by 3 |

## Results

All three programs integrate from **0 to 1 with n = 6**. I chose 6 because it is
both even and divisible by 3, so every rule can use the same `n` and the results are
directly comparable.

| Rule | Result | Error against true value |
|---|---|---|
| Trapezoidal | 0.8339 | 0.0018 |
| Simpson's 1/3 | 0.8357 | 0.0000 |
| Simpson's 3/8 | 0.8357 | 0.0000 |

True value ≈ **0.835649**. Both Simpson rules are accurate to four decimal places
with the same six sub-intervals, while the Trapezoidal Rule is already wrong in the
third decimal place.

## Requirements

None - only basic Python is used.

## How to run

```bash
python trapezoidal_rule.py
python simpson_one_third_rule.py
python simpson_three_eighth_rule.py
```

Change `x0`, `xn` and `n` at the top of any file to integrate a different range, and
change `f(x)` to integrate a different function.

## Note on my implementation

Two things about my code:

1. In the Trapezoidal Rule the interior points carry a weight of **2**, because the
   `h/2` factor sits outside the bracket. Giving them a weight of 1 halves their
   contribution and produces a noticeably wrong area.
2. I set the limits as variables at the top of each file instead of reading them
   with `input()`, so the programs run straight away in VS Code.

## Documents in this folder

| File | Contents |
|---|---|
| `README.md` | This file - objective, theory, results and discussion |
| `ALGORITHM.md` | Step-by-step algorithm and pseudocode for each method |
| `OUTPUT.md` | Full console output of every program |
| `*.py` | The Python programs |

## Discussion

- Accuracy improves as `n` increases, but a very large `n` starts to accumulate
  round-off error, so there is a practical limit.
- Simpson's rules are far more accurate for the same amount of work because they fit
  curves rather than straight lines to the function.
- Simpson's 1/3 and 3/8 gave the same answer to four decimals here; 1/3 is generally
  preferred because it needs only an even `n` rather than a multiple of 3.

## Conclusion

I implemented all three integration rules in Python and used them to evaluate
`∫₀¹ dx/(1+x³)`. Comparing the results against the true value of 0.835649 showed
clearly that Simpson's rules give much better accuracy than the Trapezoidal Rule for
the same number of sub-intervals.
