def lagrange_interpolation(x, y, x_value):
    """
    Computes the interpolated value at x_value
    using the Lagrange interpolation method.
    """
    n = len(x)
    result = 0.0

    # Calculate each Lagrange basis polynomial
    for i in range(n):
        term = y[i]

        for j in range(n):
            if i != j:
                term *= (x_value - x[j]) / (x[i] - x[j])

        result += term

    return result


# Example usage
x = [5, 7, 11, 13]
y = [150, 392, 1452, 2366]
x_value = 9

interpolated_value = lagrange_interpolation(x, y, x_value)

print(f"Interpolated value at x = {x_value} is {interpolated_value:.4f}")
