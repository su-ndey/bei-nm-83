# Lab 2 - Open Methods
# Secant Method
# Equation: f(x) = x^3 - x - 2 = 0   (root is near x = 1.521)
#
# The graph at the end is optional: if matplotlib is not installed the program
# still prints all the iterations and the root, and simply skips the plot.


def f(x):
    return x**3 - x - 2


x0 = 1
x1 = 2
tolerance = 0.0001
max_iter = 100

for i in range(max_iter):

    denominator = f(x1) - f(x0)

    if denominator == 0:
        print("Division by zero encountered.")
        break

    x2 = x1 - (f(x1) * (x1 - x0)) / denominator

    print(f"Iteration {i + 1}: x = {x2}")

    # Error condition
    if abs(x2 - x1) < tolerance:
        print("Approximate root:", x2)
        break

    x0 = x1
    x1 = x2

# -----------------------------
# Graph using Matplotlib (optional)
# -----------------------------
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("\n(matplotlib is not installed - skipping the graph.)")
    print("To see the plot, run:  pip install matplotlib")
else:
    # 400 evenly spaced points from -3 to 3, built without numpy
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
