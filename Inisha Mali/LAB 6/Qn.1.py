import math

# Input the number of data points
n = int(input("Enter number of data points: "))

# Initialize summation variables
sum_x = 0
sum_Y = 0
sum_x2 = 0
sum_xY = 0

# Read data points and compute the required sums
for i in range(n):
    x = float(input(f"x[{i}] = "))
    y = float(input(f"y[{i}] = "))

    # Take the natural logarithm of y
    Y = math.log(y)

    sum_x += x
    sum_Y += Y
    sum_x2 += x ** 2
    sum_xY += x * Y

# Calculate the coefficients
B = (n * sum_xY - sum_x * sum_Y) / (n * sum_x2 - sum_x ** 2)
a = (sum_Y - B * sum_x) / n
A = math.exp(a)

# Display the exponential curve
print("\nThe exponential fit is:")
print(f"y = {A:.4f} * e^({B:.4f} * x)")
