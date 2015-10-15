import random

dice_sides = int(input("User, how many sides would you like this die to have? "))

roll_num = int(input("Ok, how many times would you like to roll the die? "))
total = 0
count = 0

while roll_num > count:
    dice_roll = random.randint(1, dice_sides)
    count += 1
    total += dice_roll
    if dice_roll != 1:
        print("*" * dice_roll + ", " + str(dice_roll) + ' dots')
    else:
        print("*" * dice_roll + ", " + str(dice_roll) + ' dot')
        
print("Total value of all rolls: " + str(total))