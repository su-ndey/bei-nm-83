#bisection method
import math

def f(x):
    return x*math.sin(x) + math.cos(x)

#input a,b,tol,max_iter

a=float(input("enter a: "))
b=float(input("enter b: "))
tol=float(input("enter the tolerance: "))
max_iter=int(input("enter the maximum number of iterations: "))

# if f(a)*f(b)<0 then stop else continue
#calculate c and f(c) and replace with a or b

if f(a)*f(b)<0:
    print("the root lies between a and b")
else:    print("the root does not lie between a and b")


for i in range(max_iter):
     c=(a+b)/2
     if f(c)==0:
         print("the root is: ",c)
         break
     elif f(a)*f(c)<0:
         b=c
     else:
         a=c
     if abs(b-a)<tol:
         print("the root is: ",c)
         break
     
     