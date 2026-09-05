# Michael  Baker
# 9/5/26
# P4LAB2
# This program will take a number input by the user, and use it in a multiplation sequence 
# until multiplying it by the number 12. It will then ask if the user wants to repeat the program with a new number.

#Sets the inital input to "Yes" to make the while loop always run at least once 
Answer = "Yes"
#This sets the while loop to check if the answer to "Do you want to run the program again" was yes, and if it was, it loops back to the start, if not, 
# it ends the loop and continues to the next command.
while Answer == "Yes":
    num = int(input("Enter an integer: "))
    if (num >= 0):  # This makes sure the integer is a positive number, and if it is, then it runs through all the multiplication, if not, it states that it cannot run.
        print(num, "* 1= ", num * 1)
        print(num, "* 2= ", num * 2)
        print(num, "* 3= ", num * 3)
        print(num, "* 4= ", num * 4)
        print(num, "* 5= ", num * 5)
        print(num, "* 6= ", num * 6)
        print(num, "* 7= ", num * 7)
        print(num, "* 8= ", num * 8)
        print(num, "* 9= ", num * 9)
        print(num, "* 10= ", num * 10)
        print(num, "* 11= ", num * 11)
        print(num, "* 12= ", num * 12)

        Answer = input("Would you like to run the program again? ") # This is what tells the variable of answer to stay the same or change and decides if the while loop goes again.
    else:
        print("This program does not handle negative numbers")
        Answer = input("Would you like to run the program again? ")
# This runs after the loop ends and signifies the end of the program
print()
print("Exiting program...")