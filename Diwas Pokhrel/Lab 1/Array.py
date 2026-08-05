size = int(input("Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f'Enter the element {i}: '))
    array.append(element)
print("Array is:", array)
