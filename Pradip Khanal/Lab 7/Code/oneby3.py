def f(x):
    return 1 / (1 + x**3)


# Input
x0 = float(input("Enter lower limit: "))
xn = float(input("Enter upper limit: "))
n = int(input("Enter even number of subintervals: "))

# Check if n is even
if n % 2 != 0:
    raise ValueError("n must be even")

# Step size
h = (xn - x0) / n

# Simpson's 1/3 Rule
result = f(x0) + f(xn)

for i in range(1, n):
    x = x0 + i * h
    if i % 2 == 0:
        result += 2 * f(x)
    else:
        result += 4 * f(x)

# Calculate area
area = (h / 3) * result

# Output
print(f"Area under curve: {area:.4f}")