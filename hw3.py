#car dealership inventory application

vehicle_inventory = []
vehicle_dict = {}

def show_menu():
    print("\n")
    menu_options = ("Exit the program", "Display vehicle inventory (model and number)", "Add a new vehicle model", "Delete a vehicle model", 'Change vehicle inventory amount')
    for index, item in enumerate(menu_options):
        print(index, item)
        continue
            
def add_vehicle(vehicle):
    vehicle_inventory.append(vehicle)

def del_vehicle(vehicle):
    vehicle_inventory.remove(vehicle)    

def start_menu():
    while True:
        show_menu()
        menu_selection = input("Hello, please choose an option from the menu above.")
        if menu_selection == '0':
            break
        elif menu_selection == '1':
            if vehicle_inventory:
                for index, item in enumerate(vehicle_inventory):
                    print("\n")
                    print(vehicle_dict[item], item) 
                continue
            else:
                print("\n","Sorry, there are no items in the inventory yet. Please make another selection.")
        elif menu_selection == '2':
            new_vehicle = input("What is the name of the vehicle you are adding? ")
            if new_vehicle not in vehicle_inventory:
                quantity = int(input('How many ' + new_vehicle + "s do you want to add? " ))
                if (quantity >= 1): 
                    vehicle_dict[new_vehicle] = quantity
                    print("\n", "Vehicle Inventory updated.")
                    add_vehicle(new_vehicle)
                else:
                    print("That isn't a valid entry.")
            else:
                print(new_vehicle + "already exists in the inventory.")
            continue
        elif menu_selection == '3':
            if vehicle_inventory:
                for item in vehicle_inventory:
                    print(item)
                removal = input('Which of the above vehicles would you like to delete?')
                if removal in vehicle_inventory:
                    del_vehicle(removal)
                    print(removal, " was removed from the inventory")
                else:
                    print(removal, " isn't in the inventory.")
                continue
            else:
                print("Sorry, there are no vehicles in the inventory.")
        elif menu_selection == '4':
            if vehicle_inventory:
                for item in vehicle_dict:
                    print(item)
                #print(vehicle_inventory)
                vehicle = input("Which of the above vehicles' quantity do you want to change?")
                if vehicle in vehicle_dict:
                    quantity = input("What's the new quantity?")
                    if (int(quantity) >= 1.0):
                        try:
                            vehicle_dict[vehicle] = quantity
                            print("\n" + "The quantity of " + vehicle + 's has been updated.')
                        except:
                            print("That's not a number.")
                    else:
                        print("That is not a valid entry.")
                else:
                    print("\n", vehicle, " isn't in the inventory.")
            else:
                print("Sorry, there are no vehicles in the inventory.")

start_menu()
    
    