#WAP to read array of size n and display all the result from array

n=int(input("Enter the size of array: "))
arr=[]

print("enter the elements of array: ")
for i in range(n):
    elem=int(input())
    arr.append(elem)
   


#print(f'hello {a+b}')
print("the elements of array are: ")
for i in range(n):
    print(arr[i])

#for i in range(start,end,step):
