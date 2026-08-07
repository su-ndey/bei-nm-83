import math

# Input number of data points
n = int(input("Enter number of data points: "))

# Initialize sums
sum_x = 0
sum_Y = 0
sum_x2 = 0
sum_xY = 0

# Input data points
for i in range(n):
    x = float(input(f"x[{i}] = "))
    y = float(input(f"y[{i}] = "))

    # Take natural logarithm of y
    Y = math.log(y)

    sum_x += x
    sum_Y += Y
    sum_x2 += x * x
    sum_xY += x * Y

# Calculate coefficients
B = (n * sum_xY - sum_x * sum_Y) / (n * sum_x2 - sum_x ** 2)
a = (sum_Y - B * sum_x) / n
A = math.exp(a)

# Display result
print(f"\nThe exponential fit is:")
print(f"y = {A:.4f} * e^({B:.4f} * x)")