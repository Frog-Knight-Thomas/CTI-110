# Michael Baker
# 9/2/26
# P2LAB2
# Going to use this as an experiment with dictionaries by showing gas mileage and calculating how much gas is required for certain distances

mileage = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}

keys= mileage.keys()

print(keys)
car = input("What is your car? ")

MPG = mileage[car]

print("The", car, "has", MPG, "Mpg")
miles = float(input("How many miles do you want to go? "))
gas = float((miles/MPG))
print("You would need", gas, "gallons to go", miles, "miles in a", car)