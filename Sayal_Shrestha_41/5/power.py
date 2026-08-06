import numpy as np

A=np.array([[2,3,2],[3,4,1],[2,1,7]],dtype=float)

x=np.array([[1],[1],[1]],dtype=float)
max=100
e=1e-5
l_old=0

for i in range(max):
    y=np.dot(A,x)
    max_ind=np.argmax(np.abs(y))
    l_new= y[max_ind]
    x=y/l_new

    if abs(l_new-l_old)<=e:
        break
    l_old=l_new

print(f"Most dominated eigen value: {l_new}")
print(f"It's corresponding eigen vector: {x}")
