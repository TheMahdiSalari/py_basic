from math import *

####### 1
print("(ax**2) + (bx) + c =0")
a = float(input("please enter number for a : "))
b = float(input("please enter number for b : "))
c = float(input("please enter number for c : "))
delta = pow(b , 2) - (4*a*c)
if delta > 0:
    print("The equation has two roots")
    x1 = ((-b) + sqrt(delta)) / (2*a)
    x2 = ((-b) - sqrt(delta)) / (2*a)
    print("The first root has : ",x1,"\n","The second root has : ",x2)
elif delta == 0 :
    print("The equation has one root")
    x = (-b) / (2*a)
    print("The root has : ",x)
elif delta < 0:
    print("The equation has no real roots")



