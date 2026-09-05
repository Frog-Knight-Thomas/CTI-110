# Michael Baker
# 9/3/26
# P3HW1
# This is the debugged file.

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min (grades)
high = max (grades)
sum = sum(grades)
avg = (sum / 6)

# determine letter grade for average
print("------------Results------------")
print(f'{"Lowest Grade:":<25}', low)
print(f'{"Highest Grade:":<25}', high)
print(f'{"Average Grade:":<25}', avg)
print(f'{"Sum of Grades:":<25}', sum)
print("--------------------------------")


if avg >= 90:
    print('Your grade is: A')

elif avg >= 80 and avg <= 89:
    print('Your grade is: B')

elif avg >= 70 and avg <= 79:
   print('Your grade is: C')

elif avg >= 60 and avg <= 69:
   print('Your grade is: D')

elif avg >= 0 and avg <= 59:
    print('Your grade is: F') # TO DO: finish this





