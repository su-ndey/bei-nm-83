import math

n = int(input("Enter no of data points: "))
sum_x = 0
sum_Y = 0
sum_x2 = 0
sum_xY = 0

x_vals = []
y_vals = []

for i in range(n):
    x = float(input(f"x[{i}] = "))
    y = float(input(f"y[{i}] = "))
    Y = math.log(y)

    sum_x += x
    sum_Y += Y
    sum_x2 += x * x
    sum_xY += x * Y

b = (n * sum_xY - sum_x * sum_Y) / (n * sum_x2 - sum_x * sum_x)
A = (sum_Y - b * sum_x) / n
a = math.exp(A)

print("\nFitted exponential curve:")
print(f"y = {a:.4f} * e^({b:.4f}x)")
