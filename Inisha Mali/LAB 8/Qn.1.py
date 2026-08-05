import math

# Function for dy/dx
def dy(x, y, z):
    return z

# Function for dz/dx
def dz(x, y, z):
    return -10 * math.sin(x)

# Initial conditions
x = 0.0
y = 0.0
z = 10.0

# Step size and number of steps
h = 0.1
steps = 10

# RK2 Method
for i in range(steps):
    k1 = h * dy(x, y, z)
    l1 = h * dz(x, y, z)

    k2 = h * dy(x + h/2, y + k1/2, z + l1/2)
    l2 = h * dz(x + h/2, y + k1/2, z + l1/2)

    y = y + k2
    z = z + l2
    x = x + h

# Display the results
print(f"After {steps} steps:")
print(f"y({x:.1f}) = {y:.6f}")
print(f"dy/dx({x:.1f}) = {z:.6f}")