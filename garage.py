""" Eryk A Grabowski                            20/09/2022 """
print('==================================')
print('|------Welcome to the Garage-----|')
print('==================================')
class VehicleDetails:
    """ Class for vehicle creation """
    def __init__(self):
        self._make = " "
        self._model = " "
        self._year = 0
        self._color = " "
        self._mileage = 0
    def add_car(self):
        try:
            self._make = input('Enter vehicle make: ')
            self._model = input('Enter vehicle model: ')
            self._year = int(input('Enter vehicle year: '))
            self._color = input('Enter vehicle color: ')
            self._mileage = int(input('Enter vehicle mileage: '))
            return True
        except ValueError:
            print('Please try entering vehicle information again using only whole numbers for mileage and year')
            return False
    def __str__(self):
        return '\t'.join(str(a) for a in [self._make, self._model, self._year, self._color, self._mileage])
    def fix_vehicle(self):
        cost = 100
        if self._mileage > 10000 or self._year > 2005:
            cost = 1000
        else:
            cost = 100
        return cost
class Car_Inventory:
    """ Class for the storing of vehicle data """
    def __init__(self):
        self.cars = []
    def add_car(self):
        vehicle = VehicleDetails()
        if vehicle.add_car() == True:
            self.cars.append(vehicle)
            print ()
            print('This vehicle has been added, Thank you')
    # Displays a table containing the data for each vehicle in the list
    def display_Car_Inventory(self):
        print('\t'.join(["", 'Make', 'Model', 'Year', 'Color', 'Mileage']))
        for idx, vehicle in enumerate(self.cars):
            print(idx + 1, end='\t')
            print(vehicle)

    def fix_vehicle(self, index):
        return self.cars[index].fixVehicle()

inventory = Car_Inventory()
while True:

    print('Choice 1: Add Vehicle to Garage')
    print('Choice 2: Delete Vehicle from Garage')
    print('Choice 3: View Current Inventory')
    print('Choice 4: Update Vehicle in Garage')
    print('Choice 5: Repair Quote')
    print('Choice 6: Quit')
    User_Choice=input('Please Enter your Choice from one of the above options: ')
    if User_Choice== "1":
        # Adding a vehicle to the list
        inventory.add_car()
    elif User_Choice== '2':
        # Deleting a vehicle from the list
        if len(inventory.cars) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        inventory.display_Car_Inventory()
        Products = int(input('Please enter the number associated with the vehicle to be removed: '))
        if Products - 1  > len(inventory.cars):
            print('This is an invalid number')
        else:
            inventory.cars.remove(inventory.cars[Products - 1])
            print ()
            print('This vehicle has been removed')
    elif User_Choice == '3':
        # Lists all the vehicles
        if len(inventory.cars) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        inventory.display_Car_Inventory()
    elif User_Choice == '4':
        # Edit of an existing vehicle in the list
        if len(inventory.cars) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        inventory.display_Car_Inventory()
        Products = int(input('Please enter the number associated with the vehicle to be updated: '))
        if Products - 1  > len(inventory.cars):
            print('This is an invalid number')
        else:
            auto_vehicle = VehicleDetails()
            if auto_vehicle.add_car() == True :
                inventory.cars.remove(inventory.cars[Products - 1])
                inventory.cars.insert(Products - 1, auto_vehicle)
                print ()
                print('This vehicle has been updated')
        # Allows user to get a quote for the cost of a repair on a vehicle
    elif User_Choice == '5':
        if len(inventory.cars) < 1:
            print('Sorry there are no vehicles currently in inventory')
            continue
        Products = int(input("Which vehicle do you need repairing?: "))
        print('The price for repair will be: ')
        print(inventory.fix_vehicle[0])
        
    elif User_Choice == '6':
        # Exits the loop and ends the program
        print('See you later!')
        break
    else:
        # User error
        print('Error: Invalid Input, please try again')
