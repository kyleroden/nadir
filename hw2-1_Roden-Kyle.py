grocery_list = []
budget = 0
total_price = 0
remaining_money = 0
new_item_price = 0

print('Welcome to the store. Type "ALL DONE" to exit the program.')

budget = float(input("What is your budget? "))

while (total_price < budget) and (new_item_price != 'ALL DONE'):
    new_item_price = input("What's the price of your item? ")
    ##NOTE: there is an if statement below, but I was told that having an if statement (with a break) within a while loop is not best practice. So instead I created a while loop with two conditions. But I know how to use an if statement.  
    ##if new_item_price == 'ALL DONE':
     ##   break
    
    grocery_list.append(float(new_item_price))
    total_price = sum(grocery_list)
    remaining_money = budget - total_price
    print("Added that price to the list. The list now has " + str(len(grocery_list)) + " items.")
    print('The total is now $' + str(round(total_price, 2)) + ' .')
    print('You have $' + str(round(remaining_money, 2)) + ' remaining.')
    continue

print('Thank you for shopping at the store. You are $' + str((total_price - budget)) + " OVER budget.")