score = float(input("Please enter student's score :"))
if score <= 9.9 :
    print("FAIL")
elif score <= 15 :
    print("GOOD")
elif score <= 18 :
    print("VERY GOOD")
elif score <= 20 :
    print("EXCELLENT")
else:
    print("INVALID GRADE")