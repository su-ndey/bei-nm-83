import math

def f(x):
    return x * math.sin(x) + math.cos(x)

lower = 2.0
upper = 3.0

def bisection_method(left, right, tol=1e-6, max_iter=100):
    f_left = f(left)
    f_right = f(right)

    if f_left * f_right > 0:
        print("This method requires the value of a and b so f(a) and f(b) must have opposite signs.")
        return None, None

    count = 0
    while count < max_iter:
        count += 1
        mid = (left + right) / 2
        f_mid = f(mid)

        if abs(f_mid) < tol or (right - left) / 2 < tol:
            return mid, count

        if f_left * f_mid < 0:
            right = mid
            f_right = f_mid
        else:
            left = mid
            f_left = f_mid

    print(f"It did not converge after {max_iter} iterations")
    return None, None

root, iterations = bisection_method(lower, upper)

print(f"Root found: {root}")
print(f"Iterations = {iterations}")