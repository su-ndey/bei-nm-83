# Function definition
def f(x):
    return 1 / (1 + x**3)

# Read input values
lower = float(input("Enter the lower limit: "))
upper = float(input("Enter the upper limit: "))
n = int(input("Enter an even number of subintervals: "))

# Check if the number of subintervals is even
if n % 2 != 0:
    print("Error: Number of subintervals must be even.")
    exit()

# Calculate step size
h = (upper - lower) / n

# Initialize the sum with the first and last terms
total = f(lower) + f(upper)

# Add the remaining terms
for i in range(1, n):
    x = lower + i * h
    if i % 2 == 0:
        total += 2 * f(x)
    else:
        total += 4 * f(x)

# Calculate the area using Simpson's 1/3 Rule
area = (h / 3) * total

# Display the result
print("Area under the curve =", round(area, 4))