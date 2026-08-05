def f(x):
    return 3*x**2+3

x0=0
xn=2
n=100
h=(xn-x0)/n
sum=f(x0)+f(xn)
for i in range(1,n):
    x=x0+i*h
    sum+=2*f(x)

area=h*sum/2
print(f"Integration is : {area}")