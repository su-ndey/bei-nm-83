import matplotlib.pyplot as plt
import numpy as np
def g(x):
    return 5/(2*x)+x/2


x=2
e=1e-5
max=100

for i in range(max):
    x1=g(x)

    if abs(x1-x)<=e:
        print(f"f({x1}) = {g(x1)})")
        break

    x=x1

else:
    print("Didn't Converge")


x=np.linspace(2,3,200)
y=g(x)
plt.figure(figsize=(9,5))
plt.plot(x,y,label="Graph of fixed point")
plt.grid(True)
plt.legend()

plt.title("FP")
plt.xlabel("x")
plt.ylabel("y")

plt.show()