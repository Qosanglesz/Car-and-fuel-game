import turtle
from screen import Screen
from road import Road
from Car import Car
from Fuel import Fuel
from AvoidObject import Hole, Truck, Dog
from DatabaseGame import Database
import random
import os
# Screen and road set up
stage = Screen()
road = Road(400, 900)
stage.init_screen()
road.make()
# Specific X and Y for random module
random_x = [-180, -140, 90, 40, 40, 90, 140, 180]
random_y = [1000, 1200, 1400, 1600, 1800, 2000, 2200]
# Objects initialization
fuels = list()
avoids = list()
player = turtle.textinput("Name", "Enter your car name: ")
p1 = Car()
truck = Truck("square", "orange", (random.choice(random_x), random.choice(random_y)))
hole = Hole("circle", "black", (random.choice(random_x), random.choice(random_y)))
dog = Dog("square", "yellow", (random.choice(random_x), random.choice(random_y)))
# for loop of object to create many
for _ in range(5):
    fuels.append(Fuel("square", "green", (random.choice(random_x), random.choice(random_y))))
for _ in range(3):
    avoids.append(truck)
    avoids.append(hole)
    avoids.append(dog)
# Part of status
road.see_score(p1)
road.see_heart(p1)
# Part controller of player
turtle.onkey(p1.control_right, 'd')
turtle.onkey(p1.control_left, 'a')
turtle.listen()
while True:
    turtle.update()  # to update frame every time
    if p1.hearts == 0:  # Show game over screen
        stage.display.screen.bgcolor("Grey")
        road.game_over(p1)
        os.system("die.wav")
        p1.speed = 0
        admin = Database(player, p1.score)
        admin.write_database()  # insert player name and score to database
        score = admin.sorted_score()
        road.score_board(score)  # show score board
        turtle.exitonclick()
    for fuel in fuels:
        fuel.move()
        if fuel.ycor() <= -300:
            fuel.goto(random.choice(random_x), random.choice(random_y))
        if fuel.collide(p1):
            p1.increase_score()
            fuel.goto(random.choice(random_x), random.choice(random_y))
            road.see_score(p1)
    for each_obj in avoids:
        each_obj.move()
        if each_obj.ycor() <= -300:
            each_obj.goto(random.choice(random_x), random.choice(random_y))
        if each_obj.collide(p1):
            p1.decrease_hearts(each_obj.damage)
            each_obj.goto(random.choice(random_x), random.choice(random_y))
            road.see_heart(p1)
