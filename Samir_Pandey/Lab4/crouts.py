import numpy as np
import matplotlib.pyplot as plt     
A = np.array([
    [2, -1 ,-2], 
    [-4, 6, 3],
    [-4, -2, 8]
    ],dtype=float)
b = np.array([-2, 9, -5], dtype=float)
n = len(A) 
u = np.eye(n)
l = np.zeros((n, n))
for i in range(n):
    
    for j in range(i, n):
        sum1 =0
        for k in range(i):
            sum1 += l[i][k] * u[k][j]
        l[i][j] = A[i][j] - sum1
    for j in range(i+1, n):
        sum2 = 0
        for k in range(i):
            sum2 += l[j][k] * u[k][i]
        u[j][i] = A[j][i] - sum2
        l[j][i] /= l[i][i]
        print("lower matrix:\n", l)                
        print("upper matrix:\n",u)
y = np.zeros(n)
for i in range(n):
    sum3 = 0
    for j in range(i):
        sum3 += l[i][j] * y[j]
    y[i] = b[i] - sum3/l[i][i]
x = np.zeros(n)
for i in range(n-1, -1, -1):
    sum4 = 0
    for j in range(i+1, n):
        sum4 += u[i][j] * x[j]
    x[i] = y[i] - sum4
    print("Solution is :\n", x)
