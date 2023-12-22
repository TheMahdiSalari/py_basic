main_work_time = 160
main_overtime = 40
work_time = int(input("Enter your work time : "))
if work_time <= 160 :
    salary = work_time * 100
    print("your salary = ", salary , "$")
elif work_time <=220 :
    overtime = work_time - 160
    salary = (main_work_time * 100) + (overtime * 50)
    print("your salary = ", salary , "$")
else :
    extra = work_time - 220
    salary = (main_work_time * 100) + (main_overtime * 50)
    print("your salary = ", salary , "$\n", "overtime not calculated = ", extra , " Hours")
    
