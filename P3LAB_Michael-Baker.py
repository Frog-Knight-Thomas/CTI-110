# Michael Baker
# 9/2/26
# P3LAB
# This will find the most efficient method of turning any sum of money into dollars, quarters, dimes, nickles, and pennies.

Cash = (input("How much money do you have? "))
Cash = float(Cash.replace("$",""))
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