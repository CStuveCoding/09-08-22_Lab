"""
Connor Stuve
09/08/2022
Description of what this program does
"""
import sys
taxOwed = 0.0
taxRate = 0.0 #Initialized this var to use in the nested if statement
incomeTax = 0.0 #initializes this var in case earned income is too large
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
  if earnedIncome <= 19900: #Both nested if statements to calulate the total income tax
    taxRate = 0.1
    incomeTax = earnedIncome * taxRate
  elif 19901 <= earnedIncome <= 81050:
    taxRate = 0.1
    incomeTax = 19900 * taxRate
    taxRate = .12
    incomeTax += (earnedIncome - 19900) * taxRate
  elif 81051 <= earnedIncome <= 172750:
    taxRate = .1
    incomeTax = 19900 * taxRate
    taxRate = .12
    incomeTax += 61150 * taxRate
    taxRate = 0.22
    incomeTax += (earnedIncome - 81050) * taxRate
  else:
    print("You make too much money. You are probably smarter than me.")
elif maritalStatus == "s":
  if earnedIncome <= 9950:
    taxRate = 0.1
    incomeTax = earnedIncome * taxRate
  elif 9951 <= earnedIncome <= 40525:
    incomeTax = 9951 * taxRate
    taxRate = .12
    incomeTax += (earnedIncome - 9951) * taxRate
  elif 40526 <= earnedIncome <= 86375:
    taxRate = .1
    incomeTax = 9950 * taxRate
    taxRate = .12
    incomeTax += 30575 * taxRate
    taxRate = 0.22
    incomeTax += (earnedIncome - 40525) * taxRate
  else:
    print("You make too much money. You are probably smarter than me.")
moneyEarned = earnedIncome - incomeTax # calculates the amount of money that the user earned
if taxRate == 0:
  print(":(")
else:
  print("This year you earned $", earnedIncome, ". You were taxed $", incomeTax, ". So you earned a total of $", moneyEarned, "this year.")