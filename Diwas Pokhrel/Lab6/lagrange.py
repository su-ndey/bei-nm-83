import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_val):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_val - x[j]) / (x[i] - x[j])
        result += term
    return result
x = [5, 7, 11, 13]
y = [150, 392, 1452, 2366]
x_val = 9
interp = lagrange_interpolation(x, y, x_val)
print(f"Interpolated value at x = {x_val} is {interp:.4f}")
x_smooth = np.linspace(min(x), max(x), 200)
y_smooth = [lagrange_interpolation(x, y, xi) for xi in x_smooth]

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', s=100, label='Data points', zorder=5)
plt.plot(x_smooth, y_smooth, 'b-', linewidth=2, label='Lagrange Interpolation')
plt.scatter([x_val], [interp], color='green', s=150, marker='*', label=f'Interpolated point ({x_val}, {interp:.4f})', zorder=5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()