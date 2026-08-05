import math

def exponential_curve_fitting(x, y):
    n = len(x)
    sum_x = 0.0
    sum_Y = 0.0
    sum_x2 = 0.0
    sum_xY = 0.0

    for i in range(n):
        Y = math.log(y[i])
        sum_x += x[i]
        sum_Y += Y
        sum_x2 += x[i] * x[i]
        sum_xY += x[i] * Y

    B = (n * sum_xY - sum_x * sum_Y) / (n * sum_x2 - sum_x ** 2)
    a = (sum_Y - B * sum_x) / n
    A = math.exp(a)

    return A, B

x = [1, 2, 3, 4, 5]
y = [0.5, 1.7, 4.5, 12.1, 33.0]

A, B = exponential_curve_fitting(x, y)
print(f"The exponential fit is: y = {A:.4f} * e^({B:.4f} * x)")
