# Michael Baker
# 9/3/26
# P3HW2
# This calculates details of an employee's pay
#Imports the tool that lets me format numbers as currency
import locale 
locale.setlocale(locale.LC_ALL, '')
#Asks the user for their information pertaining to name, pay, and hours
Name = input("Please enter your name: ")
Hours = float (input("Please enter hours worked: "))
Rate = float (input("Please enter your pay per hour: "))
#This calculates all of the pay and seperates regular pay from overtime pay, and regualar hours from overtime hours
Basepay = Rate *(( float (Hours)// 40) * 40)
Overt = (Hours % 40)
Overtpay = (Rate * 1.5) *  ((Hours % 40))
#Calculates total pay
Total = Basepay + Overtpay
# This formats and prints all of the information in a digestible way with proper spacing and symbols.
print("--------------------------------------------------------------")
print("Employee Name:   ", Name)
print() #makes space
print(f'{"Hours Worked":<15}', f'{"Pay Rate":<17}', f'{"Overtime":<13}', f'{"Overtime Pay":<15}', f'{"RegHour Pay":<13}', f'{"Gross Pay":<13}')
print("-------------------------------------------------------------------------------------------")
print(f'{Hours:<15}', f'{(locale.currency(Rate, grouping=True)) + " Per Hour":<17}', f'{Overt:<13}', f'{(locale.currency(Overtpay, grouping=True)):<15}', f'{(locale.currency(Basepay, grouping=True)):<13}', f'{(locale.currency(Total, grouping=True)):<13}')