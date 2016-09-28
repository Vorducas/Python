# Alex Hadfield, B day, block 4
# 9/7/16
# Toybox

#Madlibs (variables supplied by classmates)
print "#Madlibs (Variables supplied by classmates)"
name = "Jackson"
action = "self-destructs" 
noun = "house"
number = 7

print name, action, noun

noun = "apple"

print name, action, number, noun

print "He had", number, noun

name = "Jill"

print name, action, noun

print name, "had", number, noun

number = 6

print name,"has", number, noun, "now"

number2 = number - 1

print name, "has", number2, noun, "now"
number3 = number * 2
print "Someone doubled", name, noun,
print "Now", name, "has", number3, noun

print "#If commands"

#If
number = 5
if number > 10:
    print "Give some away"
else:
    print "Keep them all" 
print "End of Program"

#Input
print "Input Commands"

name = raw_input ("What is your name?")

age = input ("How many?")

#Time

from datetime import datetime

now = datetime.now()

now.minute
now.hour
now.second













