import math

def dy(x,y,z):
    return x*z+1

def dz(x,y,z):
    return -x*y

x=0.0
y=0.0
z=1.0
h=0.1
steps=3

for i in range(steps):
    k1=h*dy(x,y,z)
    l1=h*dz(x,y,z)
    k2=h*dy(x+h/2,y+k1/2,z+l1/2)
    l2=h*dz(x+h/2,y+k1/2,z+l1/2)
    k3=h*dy(x+h/2,y+k2/2,z+l2/2)
    l3=h*dz(x+h/2,y+k2/2,z+l2/2)
    k4=h*dy(x+h/2,y+k3/2,z+l3/2)
    l4=h*dz(x+h/2,y+k3/2,z+l3/2)

    k=(k1+2*k2+2*k3+k4)/6
    l=(l1+2*l2+2*l3+l4)/6
    x+=h
    y+=k
    z+=l

print(f"After {steps} steps: ")
print(f"y({x:.3f}) =  {y:.3f}")
print(f"dy ({x:.3f}) /dx = {z:.3f}")
