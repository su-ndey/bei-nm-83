import math

def f(x):
    return x * math.sin(x) + math.cos(x)

left = 2.0
right = 3.0

def bisection_method(low, high, tol=1e-6, max_iter=100):
    f_low = f(low)
    f_high = f(high)

    if f_low * f_high > 0:
        print("Bisection method requires the value of a and b so f(a) and f(b)must have opposite signs.")
        return None, None

    step = 1
    while step <= max_iter:
        mid = (low + high) / 2
        f_mid = f(mid)

        if abs(f_mid) < tol or (high - low) / 2 < tol:
            return mid, step

        if f_low * f_mid < 0:
            high = mid
            f_high = f_mid
        else:
            low = mid
            f_low = f_mid

        step += 1

    print(f"Will not converge after {max_iter} iterations")
    return None, None


def regula_falsi_method(low, high, tol=1e-6, max_iter=100):
    f_low = f(low)
    f_high = f(high)

    if f_low * f_high > 0:
        print("It requires the value of a and b so f(a) and f(b)  must have opposite signs.")
        return None, None

    estimate = low

    for step in range(1, max_iter + 1):
        estimate = (low * f_high - high * f_low) / (f_high - f_low)
        f_est = f(estimate)

        if abs(f_est) < tol or abs(high - low) < tol:
            return estimate, step

        if f_low * f_est < 0:
            high = estimate
            f_high = f_est
        else:
            low = estimate
            f_low = f_est

    print(f"This method did not converge after {max_iter} iterations")
    return None, None


root, iterations = regula_falsi_method(left, right)

print(f"Root found (Regula Falsi): {root}")
print(f"Iterations = {iterations}")