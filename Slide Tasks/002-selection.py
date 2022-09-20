# SELECTION & CONDITIONALS
# if "query" is true -> do this
# else if not true -> do this

from operator import truediv

colour = "purple"

if colour == "purple":
    print("Colour is Purple! ")
# Else command runs when the if command is false
else:
    print("Colour is not Purple. ")

# elif - else if, if the first query isnt true, is this next query true etc.

yourNumber = int(input("Please enter your number: "))
print(yourNumber)

# If statement check if number is less than 10, greater than 10 or equal to 10.
if yourNumber < 10:
    print("Number is less than 10")
elif yourNumber > 10:
    print("Number is bigger than 10")
# else yourNumber == 10:
else:
    print("Number is equal to 10")

# LOGICAL & NESTED IF STATEMENTS
# AND = used when more than 2 queries need to be true.
# OR = used when 1 or 2+ queries need to be true.

shape = "square"
solid = True

# When writing queries with booleans, no need to enter == True/False
if(shape == "square" and solid == True):
    print("Shape is square AND solid")
# '!=' NOT Equal to
elif(shape != "square" and solid != True):
    print("Shape is not a square and not a solid")
elif(solid):
    print("Shape is solid")
elif(not solid):
    print("Shape is not solid")

# OR - If either query on side of OR is true, run this command
if(shape == "triangle" or solid):
    print("Shape is a triangle and not solid OR shape is solid and not a triangle Or shape is solid AND a triangle")
    if(shape == "triangle" and solid):
        print("Shape is a triangle and solid")
    elif(shape == "triangle"):
        print("Shape is a triangle and not a solid")
    else:
        print("Shape is solid and not a triangle")