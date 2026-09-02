# Michael Baker
# 9/2/26
# P1HW1
# Using Mathamatical functions in python
print("--------Exponents--------")
print()

base = int(input("Enter a Base number: "))
exponent = int(input("Enter an exponent: "))
result = base ** exponent
print(base, "raised to the power of", exponent, "is", result, "!!")
print()

print("----Addition and Subtraction----")
print()

First = int(input("Enter a starting integer: "))
Second = int(input("Enter an integer to add: "))
Third = int(input("Enter an integer to subtract: "))
Final= First + Second - Third
print(First, "+", Second, "-", Third, "is equal to", Final)