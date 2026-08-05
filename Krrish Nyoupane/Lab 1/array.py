# WAP to input a data form user, store it on array and display the array
size = int(input("Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f'Enter element {i}: '))
    array.append(element)
print("The array is:", array)
