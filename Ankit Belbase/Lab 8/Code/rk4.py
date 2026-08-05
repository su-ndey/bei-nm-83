import math


def dy(x, y, z):
    return 12 * x**2 + y + z


def dz(x, y, z):
    return -10 * math.sin(x) + 2 * y + 3 * z


# Initial conditions
x = 0.0
y = 0.0
z = 10.0

# Step size and number of steps
h = 0.1
steps = 10

# Runge-Kutta 4th Order Method
for i in range(steps):
    k1 = h * dy(x, y, z)
    l1 = h * dz(x, y, z)

    k2 = h * dy(x + h / 2, y + k1 / 2, z + l1 / 2)
    l2 = h * dz(x + h / 2, y + k1 / 2, z + l1 / 2)

    k3 = h * dy(x + h / 2, y + k2 / 2, z + l2 / 2)
    l3 = h * dz(x + h / 2, y + k2 / 2, z + l2 / 2)

    k4 = h * dy(x + h, y + k3, z + l3)
    l4 = h * dz(x + h, y + k3, z + l3)

    y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    z += (l1 + 2 * l2 + 2 * l3 + l4) / 6

    x += h

# Output
print(f"After {steps} steps:")
print(f"y({x:.1f}) = {y:.6f}")
print(f"dy/dx({x:.1f}) = {z:.6f}")