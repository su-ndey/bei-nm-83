def f(x):
    return x**3 - x - 2   

def secant(x0, x1, tol, max_iter):
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Division by zero error!")
            return
        
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"Iteration {i+1}: x = {x2}")

        if abs(x2 - x1) < tol:
            print("\nRoot is approximately:", x2)
            return
        
        x0 = x1
        x1 = x2

    print("\nDid not converge within given iterations")


x0 = float(input("Enter first guess x0: "))
x1 = float(input("Enter second guess x1: "))
tol = float(input("Enter tolerance: "))
max_iter = int(input("Enter max iterations: "))

secant(x0, x1, tol, max_iter)