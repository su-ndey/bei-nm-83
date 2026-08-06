# Lab 8 (Part 1) - RK2 (Runge-Kutta 2nd order) for a second-order ODE
#   dy/dx = z
#   dz/dx = -10 sin(x)
# Initial conditions: x0 = 0, y0 = 0, z0 = 10, step size h = 0.1, 10 steps

import math


def dy(x, y, z):
    return z


def dz(x, y, z):
    return -10 * math.sin(x)


# Initial conditions
x = 0.0
y = 0.0
z = 10.0
h = 0.1
steps = 10

print(" step      x          y            dy/dx")
for i in range(steps):
    k1 = h * dy(x, y, z)
    l1 = h * dz(x, y, z)
    k2 = h * dy(x + h / 2, y + k1 / 2, z + l1 / 2)
    l2 = h * dz(x + h / 2, y + k1 / 2, z + l1 / 2)

    y += k2
    z += l2
    x += h

    print(f"{i + 1:>5}   {x:>6.2f}   {y:>10.6f}   {z:>10.6f}")

print(f"\nAfter {steps} steps:")
print(f"y({x:.1f}) = {y:.6f}")
print(f"dy/dx({x:.1f}) = {z:.6f}")
