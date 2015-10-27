#euler problem 2
#

x = 1
def fibonacci():
    x = 1
    y = 2
    z = 0
    total = 0
    
    while (x < 4000000): #on the first loop, values will be:
        if (x % 2 == 0):
            total += x
        z = x + y       #set the third number to be the sum of the previous two numbers
        x = y           #set the first number to what was previously the second number
        y = z           #set the second number to what was previously the third number
    #return(total)
    print(total)
fibonacci()
