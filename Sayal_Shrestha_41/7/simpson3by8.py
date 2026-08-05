def f(x):
    return 3*x**2+3

x0=0
xn=2
n=100
h=(xn-x0)/n

sum=f(x0)+f(xn)
for i in range(1,n):
    x=x0+i*h
    if i%3 ==0:
        sum+=2*f(x)
    else:
        sum+=3*f(x)

area=h*(3/8)*sum
print(f"Integration is : {area}")