x = int(input("Enter your number : "))
r1 = x % 2
r2 = x % 7
if r1 == 0 and r2 == 0 :
    print("is a multiple of 2 and 7")
else :
    print("is not a multiple of 2 and 7")