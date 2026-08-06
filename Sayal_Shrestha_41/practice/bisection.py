def f(x):
    return x**3-x-2

a=0
b=2
tolerance=1e-5
steps=100

if f(a)*f(b) >0:
    print("Bracketing range is invalid")
else:
    for i in range(steps):
        c=(a+b)/2

        if f(c)==0:
            print(f"Exact value found, f[{c}]=0")
            break

        if f(a)*f(c)<0:
            b=c
        else:
            a=c

        if abs(b-a)<=tolerance:
            print(f"Approximate value found f({b}) = {f(b)}")
            break

    else:
        print(f"Max iteration reached, f({b}) = {f(b)}")
