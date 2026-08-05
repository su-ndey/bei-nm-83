#false position method
import math

def f(x):
    return x*math.sin(x) + math.cos(x)

#input a,b,tol,max_iter

a=float(input("enter a: "))
b=float(input("enter b: "))
tol=float(input("enter the tolerance: "))
max_iter=int(input("enter the maximum number of iterations: "))



if f(a)*f(b)<0:
    print("the root lies between a and b")
else:    print("the root does not lie between a and b")

print("steps    a        b       f(a)        f(b)     c         f(c)")
for i in range(max_iter):
     c=((a*f(b))-(b*f(a)))/(f(b)-f(a))
  
     print(f'{i+1}       {a:.6f}  {b:.6f}  {f(a):.6f}  {f(b):.6f}  {c:.6f}  {f(c):.6f}')
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
    