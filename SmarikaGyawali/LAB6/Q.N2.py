def lagrange_interpolation(x, y, x_val):
    n = len(x)
    result = 0.0

    for i in range(n):
        term = y[i]

        for j in range(n):
            if j != i:
                term *= (x_val - x[j]) / (x[i] - x[j])

        result += term

    return result


# ---------------- MAIN PROGRAM ----------------

print("LAGRANGE INTERPOLATION PROGRAM")

n = int(input("Enter number of data points: "))

x = []
y = []

print("\nEnter data points:")

for i in range(n):
    xi = float(input(f"x[{i}] = "))
    yi = float(input(f"y[{i}] = "))
    x.append(xi)
    y.append(yi)

x_val = float(input("\nEnter value of x to interpolate: "))

result = lagrange_interpolation(x, y, x_val)

print("\n-----------------------------------")
print(f"Interpolated value at x = {x_val} is {result:.4f}")
print("-----------------------------------")