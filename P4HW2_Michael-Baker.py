# Michael Baker
# 9/5/2026
# P4HW2
# This will give information on an employees pay and hours
#This imports a module that lets me format as currency
import locale 
locale.setlocale(locale.LC_ALL, '')
#This sets the variable that determines if the loop continues or stops
RT = True
#These are varivables that store the information added by every loop so it can be displayed at the end
Count = int()
Total_Overtpay = int()
Total_Base = int()
Gross = Total_Overtpay + Total_Base
#This is the while loop itself, it works by checking if the RT variable is true or false and continues until the RT variable is set to false. The variable only gets set to false if the name enters is "Done", if it any other name it just puts it into the predetermined text to calculate and compile the pay data of the employee
while RT == True:
    Name = input("Enter employee's name or 'Done' to terminate: ")
    if Name == "Done":
        RT = False
    else:
        Hours = float (input("Please enter how many hours "+Name+" worked: "))
        Rate = float (input("What is " + Name + "'s" + " rate? " ))
        Basepay = Rate *(( float (Hours)// 40) * 40)
        Overt = (Hours % 40)
        Overtpay = (Rate * 1.5) *  ((Hours % 40))
        Total_Base += Basepay
        Total_Overtpay += Overtpay
        Count += 1 
        Total = Basepay + Overtpay

        print("--------------------------------------------------------------")
        print("Employee Name:   ", Name)
        print()
        print(f'{"Hours Worked":<15}', f'{"Pay Rate":<17}', f'{"Overtime":<13}', f'{"Overtime Pay":<15}', f'{"RegHour Pay":<13}', f'{"Gross Pay":<13}')
        print("-------------------------------------------------------------------------------------------")
        print(f'{Hours:<15}', f'{(locale.currency(Rate, grouping=True)) + " Per Hour":<17}', f'{Overt:<13}', f'{(locale.currency(Overtpay, grouping=True)):<15}', f'{(locale.currency(Basepay, grouping=True)):<13}', f'{(locale.currency(Total, grouping=True)):<13}')
#Techinally I didn't need to make this only work if RT is False, but I felt like it and it took 2 seconds. This just runs to display the information compiles from every employee's pay data and the amount of employees
if RT == False:
    print("Total number of emplyees entered:", Count)
    print("Total amount paid for overtime:", f'{(locale.currency(Total_Overtpay, grouping=True))}')
    print("Total amount paid for regular hours:", f'{(locale.currency(Total_Base, grouping=True))}')
    print("Total amount paid in gross:", f'{(locale.currency((Total_Overtpay + Total_Base), grouping=True))}')