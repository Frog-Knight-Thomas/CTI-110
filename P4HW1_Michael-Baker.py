# Michael Baker
# 9/5/2026
# P2HW1
# This program gives specifecations on a group of grades entered by the user.
#This asks how many scores the user wants to enter
times = int(input("How many scores do you want to enter? "))
#This is a secret mouskatool that will help us later by being a varible inherintly set to "True"
RT = "True"
#Creates a list named grades
grades = []
#Now the meat and potatoes: the 14 lines of code that took me WWAYY too long to figure out, this takes the RT variable and based of the state of it, 
#changes the input question. This also takes the input for the score and, if its valid, adds it to the grades list. 

while len(grades) < times:
    if RT == "True":
        t = int(input(f"Enter score #{len(grades)+1}: "))
    else:
        t = int(input(f"Enter score #{len(grades)+1} again: "))
    if (0 <= t <= 100):
        RT = "True"
    else:
        RT = "False"
    if RT == "True":
        grades += [t]
    else:
        (print("INVALID Score enetered!!!!"))
        (print("Score should between 0 and 100"))

# Calculating the info about the grades
Added = float (sum(grades))
avg = float (Added / (times))
Lowest = float (min(grades))

#outputs the info about the scores and grade
print("--------Results--------")
print(f'{"Lowest Score":<15}',":", Lowest)
print(f'{"Modified List":<15}',":", grades)
print(f'{"Scores Average":<15}',":", avg)
#Calulates the letter grade
if avg >= 90:
    print(f'{"Grade:":<15}', ": A")

elif avg >= 80 and avg <= 89:
    print(f'{"Grade":<15}', ": B")

elif avg >= 70 and avg <= 79:
   print(f'{"Grade":<15}', ": C")

elif avg >= 60 and avg <= 69:
    print(f'{"Grade":<15}', ": D")

elif avg >= 0 and avg <= 59:
    print(f'{"Grade":<15}', ": F")