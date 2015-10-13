grocery_list = []
budget = 0
total_price = 0
remaining_money = 0

print('Welcome to the store.')

budget = int(input("what is your budget?"))


while total_price < budget:
    new_item_price = int(input("what's the price of your item?"))
    print('enter "done" to stop')
      
    if new_item_price == 'done':
        break
    
    grocery_list.append(new_item_price)
    total_price = sum(grocery_list)
    remaining_money = budget - total_price
    print("Added that price to the list. It now has " + str(len(grocery_list)) + " items.")
    print('The total is now $' + str(total_price) + ' .')
    print('You have $' + str(remaining_money) + ' remaining.')
    continue
    
print('Thank you for shopping at the store, goodbye.')                     
    
