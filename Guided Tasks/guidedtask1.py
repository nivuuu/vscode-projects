# Guided Task 1: Python Programming Basics | DOL4 A2.1 |                    Eryk A Grabowski  12/09/2022
print("Hello World!")

username= "Bob"
age = 32
# print(username,'is',age,'years old') First Version
# print(username, " is " +age+  " years old ") Second Version - This wont work as the + causes an error as you are trying to concatenate string and ints together
print(username+' is '+str(age)+' years old ') # Final version - This will work as age is being read as a string with the str fuction
