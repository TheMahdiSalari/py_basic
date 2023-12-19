from math import sqrt
n = int(input("Enter the number of range : "))
s = 0
ss = 0
for i in range(n+1) :
    s = s + (i**2)
    ss = sqrt(s)
print("(Sum of squares of numbers)----->")
print("S = ", s)
print("(The sqrt of the sum of squares of numbers)----->")
print("SS = ", ss)

