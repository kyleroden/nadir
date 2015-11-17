from turtle import *
import random

global score
score = 0
global t
t = Turtle()

def draw_board(width, height):
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.up()
    t.setpos(0, -230)
    t.down()
    t.forward(width / 2)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width / 2)

def draw_circle(width1, width2, width3):
    start_positions = [(0, -200), (0, 10), (0, 160)]
    c1 = start_positions[0]
    c2 = start_positions[1]
    c3 = start_positions[2]
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    t.up()
    t.setpos(c1)
    t.down()
    t.circle(width1, 360)
    t.up()
    t.setpos(c2)
    t.down()
    t.circle(width2, 360)
    t.up()
    t.setpos(c3)
    t.down()
    t.circle(width3, 360)
    
def tosser(): 
    t = Turtle()
    count  = 0
    global toss_num
    toss_num = int(input('Hello! Enter a number of bean bags to toss, note: number must be between 3 and 6.'))
    if (toss_num < 7 and toss_num > 2):
        #run the toss function
        toss(toss_num, 300, 500)
    else:
        print("That is not a valid number.")
    return toss_num
        
def scorer( x, y, centers, radii):
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(x,y)
    distance = t.distance(centers[0])
    #print(str(distance))
    global score
    if distance < radii[0]:
        score += 10
        #print(str(score))
    t.up()
    t.goto(x,y)
    distance = t.distance(centers[1])
    if distance < radii[1]:
        score += 20
    t.up()
    t.goto(x,y)
    distance = t.distance(centers[2])
    if distance < radii[2]:
        score += 30
    
def toss(tossCount, width, height):
    t = Turtle()
    t.hideturtle()
    bag_list = []
    centers = [(0, -125), (0, 50), (0, 180)]
    #c1 = centers[0]
    #c2 = centers[1]
    #c3 = centers[2]
    radii = [75, 40, 20]
    count = 0
    while count < toss_num:
        x = random.randint(-width / 2, width / 2)
        y = random.randint(-height / 2, height / 2)
        t.up()
        t.hideturtle()
        t.goto(x,y)
        t.pencolor('red')
        t.down()
        t.dot(20)
        #t.stamp()
        count += 1
        scorer(x,y, centers, radii )
        bag_list.append((x,y))
    t.up()
    t.goto(-30, -220)
    t.pencolor('black')
    t.write("Total score = " + str(score), move=False, align="left", font=("Arial", 16, "normal"))
    
def play_toss():
    draw_circle(75, 40, 20)
    draw_board(300, 500)
    tosser() # tosser starts the function toss, and toss starts the function scorer
    points = toss(tossCount)
    #putting this here to try to avoid using global variables
    #t.write("Total score = " + str(score), move=False, align="left", font=("Arial", 16, "normal"))
    d = input("Press enter to quit.")
    
    
play_toss()