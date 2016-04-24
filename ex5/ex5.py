name = "Cal Buelo"
age = 24 # years
height = 72 # inches
height_cm = height * 2.54
weight = 140 # lbs
weight_kg = weight * 0.45
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print "Lets talk about %s." % name
print "He's %d inches tall." % height
print "That's %d centimeters." % height_cm
print "He's %d points heavy." % weight
print "That's %d kilograms." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

#exercises
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)
print "Round 1.4893978243"
print round(1.4893978243)
print "Round 1.5893978243"
print round(1.5893978243)
