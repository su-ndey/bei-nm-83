import math
import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))
sum_x = 0
sum_Y = 0
sum_x2 = 0
sum_xY = 0
x_data = []
y_data = []
for i in range(n):
    x = float(input(f"x[{i}] = "))
    y = float(input(f"y[{i}] = "))
    x_data.append(x)
    y_data.append(y)
    Y = math.log(y)
    sum_x += x
    sum_Y += Y
    sum_x2 += x * x
    sum_xY += x * Y
B = (n * sum_xY - sum_x * sum_Y) / (n * sum_x2 - sum_x ** 2)
a = (sum_Y - B * sum_x) / n
A = math.exp(a)
print(f"The exponential fit is: y = {A:.4f} * e^({B:.4f} * x)")

# Plot the data and fitted curve
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = A * np.exp(B * x_fit)

plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, color='red', label='Data points', s=100)
plt.plot(x_fit, y_fit, 'b-', linewidth=2, label=f'Fit: y = {A:.4f}*e^({B:.4f}*x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Curve Fitting using Least Squares')
plt.legend()
plt.grid(True)
plt.show()