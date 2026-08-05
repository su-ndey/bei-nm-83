#Write the program to swap any two numbers using function
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y
a, b = swap(a, b)
print("After swapping:")
print("First number:", a)
print("Second number:", b)

