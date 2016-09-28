#Alex Hadfield, B day, Block 4
#9/13/16
#Loops, Notes
#Variables supplied by classes
from datetime import datetime
now = datetime.now()

name = "Carter"
stuff = "Pizza"
#HowMany = input("How many Pizza's?")

while now.minute < 31:
    print name, "ate a", stuff
    now = datetime.now()
    #HowMany -= 1
    
    #print 'Now he has', HowMany

for x in range(10):
    print "Logan is hungry", x


choice = yes

while choice.lower().strip() == "yes":
    print "Yeah!"
    choice = raw_input("Do you want to continue?")
