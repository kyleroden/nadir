grocery_list = []
budget = 0
total_price = 0
remaining_money = 0
new_item_price = 0

print('Welcome to the store. Type "DONE" to exit the program.')

budget = int(input("What is your budget?"))



while total_price < budget:
    new_item_price = input("What's the price of your item?")
      
    if new_item_price == 'DONE':
        break
    
    grocery_list.append(int(new_item_price))
    total_price = sum(grocery_list)
    remaining_money = budget - total_price
    print("Added that price to the list. It now has " + str(len(grocery_list)) + " items.")
    print('The total is now $' + str(total_price) + ' .')
    print('You have $' + str(remaining_money) + ' remaining.')
    continue
    
while str(new_item_price) == 'DONE':
    break
    
print('Thank you for shopping at the store, goodbye.')                     
    
