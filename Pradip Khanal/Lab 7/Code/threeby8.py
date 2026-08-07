def f(x):
    return 1 / (1 + x**3)


# Input
x0 = float(input("Enter lower limit: "))
xn = float(input("Enter upper limit: "))
n = int(input("Enter number of subintervals (divisible by 3): "))

# Check if n is divisible by 3
if n % 3 != 0:
    raise ValueError("n must be divisible by 3")

# Step size
h = (xn - x0) / n

# Simpson's 3/8 Rule
result = f(x0) + f(xn)

for i in range(1, n):
    x = x0 + i * h
    if i % 3 == 0:
        result += 2 * f(x)
    else:
        result += 3 * f(x)

# Calculate area
area = (3 * h / 8) * result

# Output
print(f"Area under curve: {area:.4f}")