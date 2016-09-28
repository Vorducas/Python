#Alex Hadfield, B Day, Block 4
#9/15/16
#Color Picker


#Accept White
#Accept Black
#Accept a few secondary colors

##Begin Program

#Version
print "Color Mixer v. 1.0.0"

#Aquire and store colors
c1 = raw_input("Enter the 1st color to mix")
c2 = raw_input("Enter the 2nd color to mix")

#Variable to determine invalid input
s = "false"

#Mix primary colors

if c1.lower().strip() == "red" and c2.lower().strip() == "yellow":
    print "Orange"
    s = "true"

if c1.lower().strip() == "yellow" and c2.lower().strip() == "red":
    print "Orange"
    s = "true"

if c1.lower().strip() == "blue" and c2.lower().strip() == "yellow":
    print "Green"
    s = "true"

if c1.lower().strip() == "yellow" and c2.lower().strip() == "blue":
    print "Green"
    s = "true"

if c1.lower().strip() == "red" and c2.lower().strip() == "blue":
    print "Violet"
    s = "true"

if c1.lower().strip() == "blue" and c2.lower().strip() == "red":
    print "Violet"
    s = "true"
#Mix secondary colors
if c1.lower().strip() == "red" and c2.lower().strip() == "orange":
    print "Vermilion"
    s = "true"

if c1.lower().strip() == "orange" and c2.lower().strip() == "red":
    print "Vermilion"
    s = "true"

if c1.lower().strip() == "orange" and c2.lower().strip() == "yellow":
    print "Amber"
    s = "true"

if c1.lower().strip() == "yellow" and c2.lower().strip() == "orange":
    print "Amber"
    s = "true"

if c1.lower().strip() == "yellow" and c2.lower().strip() == "green":
    print "Chartreuse"
    s = "true"

if c1.lower().strip() == "green" and c2.lower().strip() == "yellow":
    print "Chartreuse"
    s = "true"                                          
                                            

#Output if invalid colors were entered
if s == "false":
    print "Invalid color(s) entered"
    
