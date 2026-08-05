import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.Symbol('x')
f_expr = x**3 - x - 2
f_prime_expr = sp.diff(f_expr, x)

f = sp.lambdify(x, f_expr, 'numpy')
f_prime = sp.lambdify(x, f_prime_expr, 'numpy')

print("f(x) =", f_expr)
print("f'(x) =", f_prime_expr)

x0 = float(input("Initial guess x0 = "))
tolerance = 0.0001
max_iter = 100

x_vals = [x0]
y_vals = [f(x0)]

i = 0
while abs(f(x0)) > tolerance and i < max_iter:
    x1 = x0 - f(x0)/f_prime(x0)
    i += 1
    x0 = x1
    x_vals.append(x0)
    y_vals.append(f(x0))

print("Root approximation =", x0)
print("No of steps =", i)

x_range = np.linspace(min(x_vals) - 2, max(x_vals) + 2, 400)
plt.plot(x_range, f(x_range), label="f(x)")
plt.scatter(x_vals, y_vals, color="red", label="Newton-Raphson iterations")
plt.axhline(0, color='black', linewidth=0.8)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Newton-Raphson Method Iterations Roll: 41")
plt.legend()
plt.grid(True)
plt.show()
