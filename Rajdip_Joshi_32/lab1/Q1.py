#program to swap two numbers using function

def swap(a,b):
    temp=a
    a=b
    b=temp
    print('after swapping a=',a,'b=',b)

print('enter two numbers')
a=int(input())
b=int(input())
swap(a,b)
