# Michael Baker
# 9/2/26
# M1HW2
# This is a expenses cost calculator made in python with variable integers.

print("This Program calculates and displays travel expenses")
print()

Budget = int(input("Enter your budget: "))
Destination = input("What is your destination: ")
GasCost = int(input("How much will gas cost? "))
Hotel = int(input("How much will accomadations cost? "))
Food = int(input("How much will be spent on food? "))
Final = Budget - GasCost - Hotel - Food
print("-----Travel Expenses-----")
print("Location:", Destination)
print("Initial Budget:", Budget)
print()
print("Fuel Cost:", GasCost)
print("Hotel/Accomodation cost:", Hotel)
print("Food Cost:", Food)
print()
print("Remaining Balance:", Final)
