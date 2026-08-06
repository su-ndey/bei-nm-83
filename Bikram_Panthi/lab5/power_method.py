# Lab 5 - Power Method
# Pure Python - matrices are nested lists, no external libraries needed.
#
# Finds the dominant (largest in magnitude) eigenvalue and its eigenvector by
# repeatedly computing Y = A * X and normalising by the largest component.

A = [
    [4, 1, 0],
    [1, 20, 1],
    [0, 1, 4]
]

A = [[float(value) for value in row] for row in A]
n = len(A)


def matrix_times_vector(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def index_of_largest_magnitude(v):
    best = 0
    for i in range(1, len(v)):
        if abs(v[i]) > abs(v[best]):
            best = i
    return best


# Initial guess vector
x = [1.0, 1.0, 1.0]
tolerance = 1e-5
max_iterations = 100
lambda_old = 0.0
lambda_new = 0.0

for iteration in range(max_iterations):

    y = matrix_times_vector(A, x)

    max_idx = index_of_largest_magnitude(y)
    lambda_new = y[max_idx]

    # Normalise so the largest component becomes 1
    x = [value / lambda_new for value in y]

    if abs(lambda_new - lambda_old) < tolerance:
        break
    lambda_old = lambda_new

print(f"Dominant Eigenvalue: {lambda_new:.5f}")
print("Corresponding Eigenvector:")
for i in range(n):
    print(f"  x{i + 1} = {x[i]:.6f}")

# Verification using the Rayleigh quotient  (XT A X) / (XT X)
Ax = matrix_times_vector(A, x)
numerator = sum(x[i] * Ax[i] for i in range(n))
denominator = sum(x[i] * x[i] for i in range(n))
print(f"\nRayleigh quotient check: {numerator / denominator:.5f}")
