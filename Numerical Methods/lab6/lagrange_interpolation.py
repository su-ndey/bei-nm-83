# Lab 6 (Task 2) - Lagrange Interpolation
# P(x) = sum( y_i * L_i(x) ),  L_i(x) = product( (x - x_j)/(x_i - x_j) ) for j != i


def lagrange_interpolation(x, y, x_val):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_val - x[j]) / (x[i] - x[j])
        result += term
    return result


# Example usage:
x = [5, 7, 11, 13]
y = [150, 392, 1452, 2366]
x_val = 9

interp = lagrange_interpolation(x, y, x_val)
print(f"Interpolated value at x = {x_val} is {interp:.4f}")
