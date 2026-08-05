import math
n = int(input("Enter number of data points: "))
sum_x = 0.0
sum_Y = 0.0
sum_x2 = 0.0
sum_xY = 0.0
for i in range(n):
    x = float(input(f"x[{i}] = "))
    y = float(input(f"y[{i}] = "))
    Y = math.log(y)
    sum_x += x
    sum_Y += Y
    sum_x2 += x * x
    sum_xY += x * Y
denominator = n * sum_x2 - sum_x ** 2
if denominator == 0:
    print("Error: Denominator is zero, cannot compute fit.")
else:
    B = (n * sum_xY - sum_x * sum_Y) / denominator
    a = (sum_Y - B * sum_x) / n
    A = math.exp(a)
    print(f"The exponential fit is: y = {A:.4f} * e^({B:.4f} * x)")