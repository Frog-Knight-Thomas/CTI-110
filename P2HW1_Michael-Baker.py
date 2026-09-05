# Michael Baker
#  9/2/26
# P2HW1
# In this we will be creating a budgeting tool that has nicer formatting than in module 2

print("This Program calculates and displays travel expenses")
print()
Budget = int(input("Enter your budget: "))
Destination = input("What is your destination: ")
GasCost = int(input("How much will gas cost? "))
Hotel = int(input("How much will accomadations cost? "))
Food = int(input("How much will be spent on food? "))
Final = Budget - GasCost - Hotel - Food

import locale
locale.setlocale( locale.LC_ALL, '' )
'English_United States.1252'

print("---------Travel Expenses---------")
print(f'{"Location:":<25}', Destination)
print(f'{"Initial Budget:":<25}', locale.currency( Budget, grouping=True ))
print(f'{"Fuel Cost:":<25}', locale.currency( GasCost, grouping=True ))
print(f'{"Accomodation cost:":<25}', locale.currency( Hotel, grouping=True ))
print(f'{"Food Cost:":<25}', locale.currency( Food, grouping=True ))
print("-----------------------------------")
print(f'{"Remaining Balance:":<25}', locale.currency( Final, grouping=True ))
