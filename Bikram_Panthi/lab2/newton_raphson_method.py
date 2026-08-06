# Lab 2 - Open Methods
# Newton-Raphson Method
# Equation: f(x) = x^3 - x - 2 = 0,  f'(x) = 3x^2 - 1
#
# The graph at the end is optional: if matplotlib is not installed the program
# still prints all the iterations and the root, and simply skips the plot.


def f(x):
    return x**3 - x - 2


def df(x):
    return 3 * x**2 - 1


x0 = 1.5
tolerance = 0.0001
max_iter = 100

for i in range(max_iter):

    derivative = df(x0)

    if derivative == 0:
        print("Derivative became zero.")
        break

    x1 = x0 - f(x0) / derivative

    print(f"Iteration {i + 1}: x = {x1}")

    # Error condition
    if abs(x1 - x0) < tolerance:
        print("Approximate root:", x1)
        break

    x0 = x1

# -----------------------------
# Graph using Matplotlib (optional)
# -----------------------------
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("\n(matplotlib is not installed - skipping the graph.)")
    print("To see the plot, run:  pip install matplotlib")
else:
    start, stop, points = -3.0, 3.0, 400
    step = (stop - start) / (points - 1)
    x = [start + i * step for i in range(points)]
    y = [f(v) for v in x]

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="f(x) = x^3 - x - 2")
    plt.axhline(0)
    plt.grid(True)
    plt.legend()

    plt.title("Graph of Nonlinear Equation")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.show()
