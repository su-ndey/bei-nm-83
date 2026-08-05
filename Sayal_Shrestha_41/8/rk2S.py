import math

def dy(x,y,z):
    return x*z+1

def dz(x,y,z):
    return -x*y

x=0.0
y=0.0
z=1.0
h= 0.1
steps= 2

for i in range(steps):
    k1=h*dy(x,y,z)
    l1=h*dz(x,y,z)
    k2=h*dy(x+h/2,y+k1/2,z+l1/2)
    l2=h*dz(x+h/2,y+k1/2,z+l1/2)

    x+=h
    y+=k2
    z+=l2

print(f"After {steps} steps: ")
print(f"y({x:.3f}): {y:.3f}")
print(f"dy/dx {x:.3f} = {z:.3f}")