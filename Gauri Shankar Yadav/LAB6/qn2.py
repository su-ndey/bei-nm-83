import matplotlib.pyplot as plt
import numpy as np

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

# Example usage
x = [5, 7, 11, 13]
y = [150, 392, 1452, 2366]
x_val = 9

interp = lagrange_interpolation(x, y, x_val)
print(f"Interpolated value at x = {x_val} is {interp:.4f}")

# Plotting
x_range = np.linspace(min(x), max(x), 200)
y_range = [lagrange_interpolation(x, y, xi) for xi in x_range]

plt.scatter(x, y, color="blue", label="Data points")
plt.plot(x_range, y_range, color="red", label="Lagrange polynomial")
plt.scatter([x_val], [interp], color="green", marker="x", s=100, label=f"Interpolated at x={x_val}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange Interpolation")
plt.legend()
plt.grid(True)
plt.show()
