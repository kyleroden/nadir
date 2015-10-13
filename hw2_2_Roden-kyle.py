total_cost = 0
budget = 0
print("Welcome to ConglomoMart.")
budget = int(input("What's yer budget pardner?"))


if budget >= total_cost:
        new_item = int(input("Please enter the price of the item. Type 'done' to quit."))
        grocery_list = []
        grocery_list.append(new_item)
        total_cost = sum(grocery_list)
        print(len(grocery_list))
continue

elif new_item == "done":
    break
    
else
    break
    
print("Your total is $" + total_cost + ".")