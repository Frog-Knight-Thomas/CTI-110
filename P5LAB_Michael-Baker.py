#Michael Baker
# 9/6/26
# P5LAB
# This simulates a self-checkout counter that takes cash and gives the most efficient cash back possible.
#imports the tool that lets you use a random number generator
import random
# Defines the change function for later use.
def change(Cash):
    if Cash > 0:
        Money = Cash * 100

        Dollars = Money // 100
        Dollars2 = int(Dollars)
        Money %= 100

        Quarters = Money // 25
        Quarters2 = int(Quarters)
        Money %= 25

        Dimes = Money // 10
        Dimes2 = int(Dimes)
        Money %= 10

        Nickels = Money // 5
        Nickels2 = int(Nickels)
        Money %= 5

        Pennies = int(Money)
        if Dollars > 0:
            if Dollars > 1:
                print(Dollars2, "Dollars")
            else:
                print(Dollars2, "Dollar")
        else:
            pass
        if Quarters > 0:
            if Quarters > 1:
                print(Quarters2, "Quarters")
            else:
                print(Quarters2, "Quarter")
        else:
            pass
        if Dimes > 0:
            if Dimes > 1:
                print (Dimes2, "Dimes")
            else:
                print (Dimes2, "Dime")
        else:
            pass
        if Nickels > 0:
            if Nickels > 1:
                print(Nickels2, "Nickels")
            else:
                print(Nickels2, "Nickel")
        else:
            pass
        if Money > 0:
            if Pennies > 1:
                print(Pennies, "Pennies")
            else:
                print(Pennies, "Penny")
        else:
            pass
    else:
        print("No Change")

#Defines the main function that prints all the questions and get the inputs for information. Also generates the random price. Runs the change function and supplies the variable it needs to run.
def main():
    Cost = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${Cost: .2f}")
    Cash = (input("How much cash will you put in the self-checkout? "))
    Cash = float(Cash.replace("$",""))
    t = (Cash - Cost)
    print(f"Change is: ${(t): .2f}")
    change(t)
#Runs the main function
main()