import numpy as np

def power_method(A, num_iterations: int = 100, tol: float = 1e-6):
    n, m = A.shape
    if n != m:
        raise ValueError("Matrix must be square")

    # Start with a random vector
    b_k = np.random.rand(n)

    for _ in range(num_iterations):
        # Multiply by matrix
        b_k1 = np.dot(A, b_k)

        # Normalize the vector
        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm

        # Rayleigh quotient gives eigenvalue approximation
        eigenvalue = np.dot(b_k.T, np.dot(A, b_k))

        # Check convergence
        if np.linalg.norm(np.dot(A, b_k) - eigenvalue * b_k) < tol:
            break

    return eigenvalue, b_k

# Example usage
A = np.array([
    [2, 1],
    [1, 3]
], dtype=float)

dominant_eigenvalue, eigenvector = power_method(A)
print("Dominant Eigenvalue:", dominant_eigenvalue)
print("Corresponding Eigenvector:", eigenvector)