
def f(x):
    return x**3 - x - 2


# Initial interval
a = 1
b = 2

# Parameters
tolerance = 0.0001
max_iter = 100

# Check if root is bracketed
if f(a) * f(b) >= 0:
    print("Invalid interval. Root is not bracketed.")
else:
    for i in range(max_iter):

        # Midpoint
        c = (a + b) / 2

        print(f"Iteration {i + 1}: c = {c}")

        # Exact root found
        if f(c) == 0:
            print("Exact root found:", c)
            break

        # Root lies in left interval
        elif f(a) * f(c) < 0:
            b = c

        # Root lies in right interval
        else:
            a = c

        # Check stopping condition
        if abs(b - a) < tolerance:
            print("Approximate root:", c)
            break

    else:
        print("Maximum iterations reached.")
        print("Approximate root:", c)