import math
import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))
sum_x = sum_Y = sum_x2 = sum_xY = 0
x_vals = []
y_vals = []

for i in range(n):
    x = float(input(f"x[{i}] = "))
    y = float(input(f"y[{i}] = "))
    if y <= 0:
        raise ValueError("y must be positive for log transformation")
    log_y = math.log(y)
    sum_x += x
    sum_Y += log_y
    sum_x2 += x * x
    sum_xY += x * log_y
    x_vals.append(x)
    y_vals.append(y)

# Regression coefficients
B = (n * sum_xY - sum_x * sum_Y) / (n * sum_x2 - sum_x**2)
a = (sum_Y - B * sum_x) / n
A = math.exp(a)

print(f"The exponential fit is: y = {A:.4f} * e^({B:.4f} * x)")

# Plotting
x_range = np.linspace(min(x_vals), max(x_vals), 200)
y_fit = A * np.exp(B * x_range)

plt.scatter(x_vals, y_vals, color="blue", label="Data points")
plt.plot(x_range, y_fit, color="red", label="Exponential fit")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Exponential Regression Fit")
plt.legend()
plt.grid(True)
plt.show()
