from math import *

print("(a**2) + (b*x) + c = 0")
a = float(input("please enter number for a :"))
b = float(input("please enter number for b :"))
c = float(input("please enter number for c :"))
delta = pow(b,2) - (4*a*c)
if delta > 0 :
    print("The equation has two roots")
    x1 = ((-b) + sqrt(delta)/(2*a))
    x2 = ((-b) - sqrt(delta)/(2*a))
    print("the first root is : ",x1,"\n","The second root is : ",x2)
elif delta == 0 :
    print("The equation has one root")
    x = (-b) / (2*a)
    print("The root is : ",x)
elif delta < 0 :
    print("The equation has no real roots")