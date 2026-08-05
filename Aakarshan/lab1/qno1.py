def f(x):
    return x**3 - x - 2
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
tolerance = 0.001
max= 100
if f(a) * f(b) >= 0:
    print("Invalid interval. Root is not bracketed.")
else:
    for i in range(max):
        c = (a + b) / 2

        if f(c) == 0:
            print("Exact root found:", c)
            print("Number of iterations:", i + 1)
            break

        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        if abs(b - a) < tolerance:
            print("Approximate root:", c)
            print("Number of iterations:", i + 1)
            break