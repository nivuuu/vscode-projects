# Iteration - repeating a block of code for ease of development

# While loop
counter = 1
while counter < 10:
    # Casting our integer into a string for the print function
    print(f"Value of counter: {counter}")
    # To stop a code from CTRL + C
    # counter = counter + 1
    counter += 1

counter2 = 1
while counter2 > 10:
    print(f"Value of counter: {counter2}")
    counter2 += 1

counter3 = 1
while counter3 > 0:
    print(f"Value of counter: {counter3}")
    counter3 += 1

colour = "red"
while colour != "orange":
    colour = input("Please enter a coour: ")
    print (f"Current value of colour: {colour}")

