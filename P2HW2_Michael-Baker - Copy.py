# Michael Baker
# 9/2/26
# P2HW2
# Will take grade inputs fro each module and tell the user the lowest, highest, average, and sum of the integers provided.

#Note: Make sure to add pseudocode (details about your program) to your script. 
#You can do this by adding the whole process as one doc string at the top of your script or as comments throughout your script. Either way is fine! 

#This just asks for the grades and assigns them variables for later
print("Please enter the grade for each module:")
m1 = float(input("Module 1: "))
m2 = float(input("Module 2: "))
m3 = float(input("Module 3: "))
m4 = float(input("Module 4: "))
m5 = float(input("Module 5: "))
m6 = float(input("Module 6: "))

#This puts the grades into a list
Grades = [m1, m2, m3, m4, m5, m6]

#Getting the lowest, highest, average, and sum of the grades
Lowest = min(Grades)
Highest = max(Grades)
Average = (sum(Grades)/6)
Sum = sum(Grades)

#This prints out all of the calculated information
print("------------Results------------")
print(f'{"Lowest Grade:":<25}', Lowest)
print(f'{"Highest Grade:":<25}', Highest)
print(f'{"Average Grade:":<25}', Average)
print(f'{"Grade Total:":<25}', Sum)
print("--------------------------------")
