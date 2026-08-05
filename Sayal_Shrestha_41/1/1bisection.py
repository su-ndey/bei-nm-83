
def f(x):
    return x**3 - x -2
a= float(input('a= '))
b= float(input('b= '))
tolerance = 0.0001
max=100
c=(a+b)/2
if (f(c)==0):
        print(f'{c} is the Exact value ')
else:
    i=0
    while(abs(b-a)>tolerance):
        c=(a+b)/2
        i+=1
        if(f(a)*f(c)<0):
            b=c
        else:
            a=c
        if (i==max):
            break;
print(f'x= {a}')
print(f'No of steps = {i}')