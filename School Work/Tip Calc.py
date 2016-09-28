# Alex Hadfield, B day, block 4
# 9/9/16

#Importing and setting up the clock
from datetime import datetime
now = datetime.now()

#Version
print "Tip Calculator v. 1.1.0"

#Changelog
#-Added custom tax % input

#Getting the user's name
n = raw_input ("What is your name?")

#Tip Calculator 
p = input ("Please enter the percent you would like to tip without a percentage sign.")
c = input ("Please enter the cost of your purchase in USD")

pt = p * .01
t = c * pt

#Tax Calculator
tax = c * .07

#Total Cost
tc = c + t + tax

#Output
print "Tip: ", "$",t
print "Tax: ", "$",tax
print "Total Cost: ", "$",tc
print "Time of output", now.hour,":",now.minute
print "Have a good day,", n




