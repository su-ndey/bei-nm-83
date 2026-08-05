import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x * math.sin(x) + math.cos(x)

def df(x):
    return x * math.cos(x)

x0 = 2.0

def newton_raphson(x0, tol=0.000001, max_iter=100):
    x = x0
    
    for iteration in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-15:
            print("Division by zero in Newton-Raphson method")
            return None, None
        
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tol and abs(f(x_new)) < tol:
            return x_new, iteration
        
        x = x_new
    
    print(f"Newton-Raphson method did not converge after {max_iter} iterations")
    return None, None

root, iterations = newton_raphson(x0)
print(f"Root found: {root}")
print(f"Iterations = {iterations}")

x = np.linspace(-2, 5, 1000)
y = [f(xi) for xi in x]

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.plot(root, f(root), 'ro', markersize=6)
plt.plot(x0, f(x0), 'go', markersize=4)
plt.grid(True)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Newton-Raphson Method for Finding Root of xsin(x) + cos(x)')
plt.show()
