
def f(x):
    return x**3 - x -2
a= float(input('a= '))
b= float(input('b= '))
tolerance = 0.0001
max=100
c=(a*f(b)-b*f(a))/(f(b)-f(a))
if (f(c)==0):
        print(f'{c} is the Exact value ')
else:
    i=0
    cl=a
    while(abs(cl-c)>tolerance):
        i+=1
        print(c)
        a=c 
        cl=c
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        if (i==max):
             break;

print(f'x= {a}')
print(f'No of steps = {i}')