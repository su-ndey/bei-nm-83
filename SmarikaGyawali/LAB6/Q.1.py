import math

n = int(input("Enter number of data points: "))

sum_x = 0
sum_Y = 0
sum_x2 = 0
sum_xY = 0

for i in range(n):
    x = float(input(f"Enter x[{i}]: "))
    y = float(input(f"Enter y[{i}]: "))

    if y <= 0:
        print("Error: y must be positive for logarithm.")
        exit()

    Y = math.log(y)

    sum_x += x
    sum_Y += Y
    sum_x2 += x * x
    sum_xY += x * Y

den = (n * sum_x2 - sum_x ** 2)

if den == 0:
    print("Error: Division by zero (invalid data).")
else:
    B = (n * sum_xY - sum_x * sum_Y) / den
    a = (sum_Y - B * sum_x) / n
    A = math.exp(a)

    print("\nExponential Curve Fit Result:")
    print(f"y = {A:.4f} * e^({B:.4f} * x)")