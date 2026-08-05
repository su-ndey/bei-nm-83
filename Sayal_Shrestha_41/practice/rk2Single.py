import math

def dy(x,y):
    return 2*y/x

x=1
y=2
h=0.25
n=4

for i in range(n):
    m1=dy(x,y)
    m2=dy(x+h, y+m1*h)
    m=(m1+m2)/2
    x+=h
    y+=m*h

print(f"y({x:.3f})= {y:.3f}")
