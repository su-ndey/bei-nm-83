def f(x):
    return 3*x**2+3

x0=0
xn=2
n=100
h=(xn-x0)/n
if n%2 != 0:
    raise ValueError("Even required")
sum=f(x0)+f(xn)
for i in range(1,n):
    x=x0+i*h
    if i%2 ==0:
        sum+=2*f(x)
    else:
        sum+=4*f(x)

area=h*sum/3
print(f"Integration is : {area}")