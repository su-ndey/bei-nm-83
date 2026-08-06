import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 - x - 2

a = float(input('a='))
b = float(input('b='))
tolerance = 0.0001
max_iter = 100

c = (a*f(b) - b*f(a)) / (f(b) - f(a))
x_vals = [a, b]
y_vals = [f(a), f(b)]

if f(c) == 0:
    print(f'{c} is the Exact value ')
else:
    i = 0
    while abs(b - a) > tolerance:
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        i += 1
        a= b
        b=c
        x_vals.append(c)
        y_vals.append(f(c))
        if i == max_iter:
            break

print(f'x= {a}')
print(f'No of steps = {i}')

# Plotting the function
x = np.linspace(min(x_vals) - 2, max(x_vals) + 2, 400)
plt.plot(x, f(x), label='f(x)')
plt.axhline(0, color='black', linewidth=0.8)

# Plotting secant iterations
plt.scatter(x_vals, y_vals, color='red', label='Secant iterations')
plt.plot(x_vals, y_vals, '--', color='orange')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Secant Method Iterations Roll: 41')
plt.legend()
plt.grid(True)
plt.show()
