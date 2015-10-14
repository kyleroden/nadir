grocery_list = []
budget = 0
total_price = 0
remaining_money = 0
new_item_price = 0

print('Welcome to the store. Type "ALL DONE" to exit the program.')

budget = float(input("What is your budget? "))

while (total_price < budget) and (new_item_price != 'ALL DONE'):
    new_item_price = input("What's the price of your item? ")
      
    ##if new_item_price == 'ALL DONE':
     ##   break
    
    grocery_list.append(float(new_item_price))
    total_price = sum(grocery_list)
    remaining_money = budget - total_price
    print("Added that price to the list. The list now has " + str(len(grocery_list)) + " items.")
    print('The total is now $' + str(total_price) + ' .')
    print('You have $' + str(remaining_money) + ' remaining.')
    continue

print('Thank you for shopping at the store. You are $' + str(total_price - budget) + " OVER budget.")                     
    
