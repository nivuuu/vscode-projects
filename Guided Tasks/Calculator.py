def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

print("Select a mode")
print("1. Add  + ")
print("2. Subtract  - ")
print("3. Multiply  * ")
print("4. Divide  / ")
print("5. Power ** ")

while True:
    choice = input("Enter your selection(1/2/3/4/5): ")
    
    if choice in ("1", "2", "3", "4", "5"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == "5":
            print(num1, "**", num2, "=", power(num1, num2))

        next_calc = input("Another calculation? (Y/N): ")
        if next_calc == "N":
            break
    else:
        print("Invalid Input, please try again")




    

