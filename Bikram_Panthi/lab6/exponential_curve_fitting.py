# Lab 6 (Task 1) - Exponential Curve Fitting by Least Squares
# Fits y = A * e^(Bx) by taking logs:  ln y = ln A + Bx  ->  Y = a + Bx
#   B = (n*sum(xY) - sum(x)*sum(Y)) / (n*sum(x^2) - (sum(x))^2)
#   a = (sum(Y) - B*sum(x)) / n      and     A = e^a

import math

# Sample data points (change these to the values given in your exam / lab sheet)
x_data = [1, 2, 3, 4]
y_data = [1.65, 2.70, 4.50, 7.35]

n = len(x_data)
sum_x = 0
sum_Y = 0
sum_x2 = 0
sum_xY = 0

for i in range(n):
    x = float(x_data[i])
    y = float(y_data[i])
    Y = math.log(y)

    sum_x += x
    sum_Y += Y
    sum_x2 += x * x
    sum_xY += x * Y

B = (n * sum_xY - sum_x * sum_Y) / (n * sum_x2 - sum_x**2)
a = (sum_Y - B * sum_x) / n
A = math.exp(a)

print(f"The exponential fit is: y = {A:.4f} * e^({B:.4f} * x)")

# Fitted values against the given data
print("\n   x        y (given)    y (fitted)")
for i in range(n):
    y_fit = A * math.exp(B * x_data[i])
    print(f"{x_data[i]:>4}   {y_data[i]:>10.4f}   {y_fit:>10.4f}")
