# Create a comment with a '#'
# TComments won't run, their purpose is to explain whats going on within a program

# Python is an interpreted language that reads top to bottom
# print('will this work?')
# With VSCode highlighting / selecting a line then pressing CTRL + / will comment or uncomment the selected text
print('Hello World')
print('Now me!')

# ====== VARIABLES AND DATA TYPES ======
# Variables - stand in for data, you can change them to impact or update a program

# With Python variables you do not need to specify the type of data before creating it
# Booleans are case sensitive, has to be positive or negative, true or false.
booleanVar = True
floatVar = 1.5
intVar = 1
# Text an be "" or ''
string = "Text"
# Example of a list
listVar = ["Mango", "Kiwi", "Appple"]

# When compiling, Python will understand that this is an integer or int
Age = 25
print(Age)
print(listVar)

# Inputs allow the user to interact with the terminal and enter values
# Example of getting data from the user with the variable username
username = input("Please enter Username: ")
favColour = input("Please enter a colour: ")
print(username)
print(favColour)

# When using inputs the value is ALWAYS a String
# Unless we use CASTING to change the type of data
favNumber = int(input("Please enter your favourite number: "))
newNumber = favNumber + 1
print(newNumber)




