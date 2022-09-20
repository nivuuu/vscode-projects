
# number = int(input("Please input a whole number: "))
# counter = number - 1

# while counter > 1:
#     number = number * counter
#     counter -= 1

# While Loop

number = int(input("Please enter a number: "))
counter = 1
value = 1
while counter <= number:
    value = value * counter
    counter += 1
print(f"Factorial of {number} is {value}")
    

# For Loop
value = 1
for x in range(1, number + 1):
    value = value * x
print(f"Factorial of {number} is {value}")

# Investment Loop
startValue = 100
goal = 1000
interest = 1.1 #110%
months = 0
currentValue = startValue

while currentValue <= 1000:
    # Increase current value by interest
    currentValue = currentValue * interest
    months += 1

print(f"Took {months} months to turn {startValue} into {goal}")
