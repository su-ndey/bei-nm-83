import math
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x**3-2*x-5

a=-2
b=1
n=100
e=1e-5

for i in range(n):
 
    if f(b)-f(a) == 0:
        raise ValueError("Divide by 0")
    c=b- (f(b)*(b-a))/(f(b)-f(a))
    if f(c)==0:
        print(f"Exact value found, f({c}) = {f(c)}")
        break
    a=b
    b=c
    if abs(b-a) <=e:
        print(f"Approximate value f({c:.3f}) = {f(c):.3f}")
        break

else:
    print(f"The value doesn't converge f({c}) = {f(c)}")

x=np.linspace(-5,5,400)
y=f(x)

plt.figure(figsize=(9,5))
plt.plot(x,y,label="Secant Method 41")
plt.grid(True)
plt.legend()

plt.title("Secant M")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color="cyan")

plt.show()