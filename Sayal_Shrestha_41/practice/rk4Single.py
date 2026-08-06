def dy(x,y):
    return 2*y/x

x=1
y=2
h=0.5
n=2

for i in range(n):
    m1=dy(x,y)
    m2=dy(x+h/2,y+m1*h/2)
    m3=dy(x+h/2,y+m2*h/2)
    m4=dy(x+h,y+m3*h)

    m=(m1+2*m2+2*m3+m4)/6
    x+=h
    y+=m*h

print(f"y({x:.3f}) = {y:.3f}")