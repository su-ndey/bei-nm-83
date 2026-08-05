import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * math.sin(x) + math.cos(x)

def df(x):
    return x * math.cos(x)

initial_guess = 2.0

def newton_raphson(start, tol=1e-6, max_iter=100):
    current = start

    step = 1
    while step <= max_iter:
        f_current = f(current)
        df_current = df(current)

        if abs(df_current) < 1e-15:
            print("Division by zero in Newton-Raphson method")
            return None, None

        next_x = current - f_current / df_current

        if abs(next_x - current) < tol and abs(f(next_x)) < tol:
            return next_x, step

        current = next_x
        step += 1

    print(f"Newton-Raphson method did not converge after {max_iter} iterations")
    return None, None

root, iterations = newton_raphson(initial_guess)

print(f"Root found: {root}")
print(f"Iterations = {iterations}")

x_values = np.linspace(-2, 5, 1000)
y_values = [f(value) for value in x_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, 'b-', linewidth=2)
plt.plot(root, f(root), 'ro', markersize=6)
plt.plot(initial_guess, f(initial_guess), 'go', markersize=4)

plt.grid(True)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Newton-Raphson Method for Finding Root of xsin(x) + cos(x)')
plt.show()