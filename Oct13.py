inventory = []


while len(inventory) < 4:
    inventory_item = input('give me some items. type "exit" to quit')
    inventory.append(inventory_item)
    for item in inventory:
        print(item)
    break

if 'exit' in inventory_item:
    print('goodbye')
