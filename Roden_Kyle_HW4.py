#Kyle Roden
#CS 161
#Homework 4, Bean Bag Toss

from turtle import *
import random

def draw_board(width, height):
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.up()
    t.setpos(0, -245)
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
    t.up()
    
def tosser():
    t = Turtle()
    t.hideturtle()
    count = 0
    try: # ensures that user gives a number
        toss_num = int(input('Hello! Enter a number of bean bags to toss. Note: number must be between 3 and 6.'))
        if toss_num < 7 and toss_num > 2: #number of bags should be between 3 and 6
            toss(toss_num, 300, 500)
        else:
            print("That is not a valid number.") 
        return toss_num
    except:
        print("That is not a valid entry.")
    
def scorer(x, y, centers, radii):
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(x, y)
    distance = t.distance(centers[0])
    score = 0
    if distance < radii[0]:
        score += 10
    t.up()
    t.goto(x, y)
    distance = t.distance(centers[1])
    if distance < radii[1]:
        score += 20
    t.up()
    t.goto(x, y)
    distance = t.distance(centers[2])
    if distance < radii[2]:
        score += 30
    return score
        
def toss(toss_num, width, height):
    t = Turtle()
    t.hideturtle()
    centers = [(0, -125), (0, 50), (0, 180)]
    radii = [75, 40, 20]
    count = 0
    total_points = 0
    while count < toss_num:
        x = random.randint(-width / 2, width / 2)
        y = random.randint(-height / 2, height / 2)
        t.up()
        t.hideturtle()
        t.goto(x, y)
        t.pencolor('red')
        t.down()
        t.dot(20)
        count += 1
        points = 0
        points = scorer(x, y, centers, radii)
        total_points += points
    t.up()
    t.goto(0, -220)
    t.pencolor('black')
    t.write("Total score = " + str(total_points), move=False, align="center", font=("Arial", 16, "normal"))
    
def play_toss():
    draw_circle(75, 40, 20)
    draw_board(300, 500)
    tosser() # tosser takes user input for number of bags and starts the function toss
    d = input("Press enter to quit.")
    
    
play_toss()