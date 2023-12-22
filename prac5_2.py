main_work_time = 160
main_overtime = 40
work_time = float(input("Enter your work time : "))
if work_time <= main_work_time :
    salary = work_time * 100
    print("Your salary = " , salary, "$")
elif work_time <= main_work_time + main_overtime :
    overtime = work_time - main_work_time
    salary = (main_work_time * 100) + (overtime * 50)
    print("Your salary = " , salary, "$")
else :
    extra_time = work_time - (main_work_time + main_overtime)
    salary = (main_work_time * 100) + (main_overtime * 50)
    print("Your salary = " , salary, "$\n",
    "Extra time not calculated = " , extra_time, "Hours")