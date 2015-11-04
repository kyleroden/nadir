vehicle_inventory = []
vehicle_dict = {}

#A list of menu options will be stored in a tuple. These menu options will be displayed to the user to indicate desired #functionality. The menu options will be: Exit the program; Display the inventory (model and number); Add a new car model; #Delete a car model; and Change the inventory (number in the lot) of a car model.

choice = None

while choice != '0':
    print(
        '''
Vehicle Inventory Program
Menu Options:
 0 - Quit
 1 - Display the inventory (model and number)
 2 - Add a new car model
 3 - Delete a car model
 4 - Change the inventory (number in the lot) of a car model
 '''
        )
    choice = input("Choose an option from the above menu.")
    #Exit the program
    if choice == '0':
        print("Farewell.")
    #print the current vehicle inventory
    elif choice == '1':
        if vehicle_dict:
            print('\n')
            for key, value in vehicle_dict.items():
                print("Vehicle Model: ", key, '\t',"Quantity: ", value)
        else:
            print("\n", "There are no vehicles in the inventory.")
    #add a new vehicle to the inventory
    elif choice == '2':
        new_vehicle = input("What is the name of the vehicle you are adding? ")
        if new_vehicle not in vehicle_inventory:
            quantity = int(input('How many ' + new_vehicle + "s do you want to add? " ))
            if (quantity >= 1): 
                vehicle_dict[new_vehicle] = quantity
                print("\n", "Vehicle inventory updated.")
                vehicle_inventory.append(new_vehicle)
            else:
                print("That is not a valid entry.")
        else:
            print(new_vehicle, ' is already in the inventory.')
    #delete a vehicle from the inventory     
    elif choice == '3':
        if vehicle_dict:
            for key, value in vehicle_dict.items():
                print("Vehicle Model: ", key, '\t',"Quantity: ", value)
            deletion = input('Which vehicle would you like to delete?')
            if deletion in vehicle_inventory:
                vehicle_inventory.remove(deletion)
                del vehicle_dict[deletion]
                print(deletion, ' was deleted from the inventory.')
            else:
                print(deletion, " is not in the inventory.")
        else:
            print("There are no vehicles in the inventory.")
    #change the quantity of a vehicle   
    elif choice == '4':
        if vehicle_dict:
            for key, value in vehicle_dict.items():
                print("Vehicle Model: ", key, '\t',"Quantity: ", value)
            change = input("Which vehicle's quantity would you like to change?")
            if change in vehicle_inventory:
                quantity = input("What is the new quantity?")
                if quantity >= 1:
                    vehicle_dict[change] = quantity
                    print("The quantity of ", change, " has been changed to ", quantity, ".")
                else:
                    print("You must enter a number that is greater than or equal to one.")
            else:
               print(change, " is not in the inventory.") 
        else:
            print("There are no vehicles in the inventory.")
            
           