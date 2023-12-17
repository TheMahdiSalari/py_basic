from math import *


def distance(x1,x2,y1,y2):
    d = sqrt((x2-x1)**2 + (y2-y1)**2)
    print("distance = ", d)

x1 =float(input("enter x1 point : "))
y1 =float(input("enter y1 point : "))
x2 =float(input("enter x2 point : "))
y2 =float(input("enter y2 point : "))
distance(x1, y1, x2, y2)
