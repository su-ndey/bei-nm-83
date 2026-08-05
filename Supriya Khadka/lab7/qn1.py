def f ( x ) :
return 1 / (1 + x **3)
x0 = float ( input ( " Enter ␣ lower ␣ limit : ␣ " ) )
xn = float ( input ( " Enter ␣ upper ␣ limit : ␣ " ) )
n = int ( input ( " Enter ␣ number ␣ of ␣ subintervals : ␣ " ) )
h = ( xn - x0 ) / n
result = f ( x0 ) + f ( xn )
for i in range (1 , n ) :
x = x0 + i * h
result += f ( x )
area = ( h / 2) * result
print ( f " Area ␣ under ␣ curve : ␣ { area :.4 f } " )
