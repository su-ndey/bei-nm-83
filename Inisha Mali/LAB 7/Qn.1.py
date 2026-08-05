def f(x):
    return 1 / (1 + x**3)


# Input values
x0 = float(input("Enter lower limit: "))
xn = float(input("Enter upper limit: "))
n = int(input("Enter number of subintervals: "))

# Step size
h = (xn - x0) / n

# Apply Trapezoidal Rule
result = f(x0) + f(xn)

for i in range(1, n):
    x = x0 + i * h
    result += 2 * f(x)

area = (h / 2) * result

# Output
print(f"Area under the curve: {area:.4f}")