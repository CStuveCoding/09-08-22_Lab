"""
Connor Stuve
09/08/2022
Description of what this program does
"""
import sys
taxOwed = 0.0
taxRate = 0.0 #Initialized this var to use in the nested if statement
earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
if earnedIncome < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()
print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")
#Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")
if maritalStatus == "m": #both used to find how much money the user kept this year
  if earnedIncome <= 19900:
    taxRate = 0.9
  elif 1990.01 <= earnedIncome <= 81050:
    taxRate = 0.88
  elif 81050.01 <= earnedIncome <= 172750:
    taxRate = 0.78
  else:
    print("You make too much money. You are probably smarter than me.")
elif maritalStatus == "s":
  if earnedIncome <= 9950:
    taxRate = 0.9
  elif 9950.01 <= earnedIncome <= 40525:
    taxRate = 0.88
  elif 40525.01 <= earnedIncome <= 86375:
    taxRate = 0.78
  else:
    print("You make too much money. You are probably smarter than me.")
income = earnedIncome * taxRate #calculates the income they kept
moneyTaxed = earnedIncome - income # calculates the amount of money that the user got taxed
if taxRate == 0:
  print("bROKEN cALCULATOR")
else:
  print("This year you earned $", earnedIncome, ". You were taxed $", moneyTaxed, ". So you earned a total of $", income, "this year.")