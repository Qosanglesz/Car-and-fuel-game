from screen import Screen
from road import Road
from Car import Car
from Fuel import Fuel
from AvoidObject import AvoidObject, Hole, Truck, Dog
from DatabaseGame import Database
import turtle
import random

stage = Screen()
road = Road(400, 900)
stage.init_screen()
road.make()

random_x = [-190, -140, 90, 40, 40, 90, 140, 190]
random_y = [600, 1000, 1200, 1400]
player = turtle.textinput("Name", "Enter your car name: ")
p1 = Car("circle", "red", position=(0, -250))
truck = Truck("square", "orange", (random.choice(random_x), random.choice(random_y)))
hole = Hole("circle", "grey", (random.choice(random_x), random.choice(random_y)))
dog = Dog("square", "yellow", (random.choice(random_x), random.choice(random_y)))
db = Database(player, p1.score)

fuels = []
for _ in range(3):
    fuels.append(Fuel("square", "green", (random.choice(random_x), random.choice(random_y))))

avoids = []
for _ in range(3):
    avoids.append(truck)
    avoids.append(hole)
    avoids.append(dog)

road.see_status(p1)
road.see_heart(p1)
turtle.onkey(p1.control_right, 'd')
turtle.onkey(p1.control_left, 'a')
turtle.listen()


while True:
    turtle.update()
    if p1.hearts == 0:
        stage.display.screen.bgcolor("Grey")
        road.game_over(p1)
        p1.speed = 0
    for fuel in fuels:
        fuel.move()
        if fuel.ycor() <= -300:
            fuel.goto(random.choice(random_x), random.choice(random_y))
        if fuel.collide(p1):
            p1.increase_score()
            fuel.goto(random.choice(random_x), random.choice(random_y))
            road.see_status(p1)
    for each_obj in avoids:
        each_obj.move()
        if each_obj.ycor() <= -300:
            each_obj.goto(random.choice(random_x), random.choice(random_y))
        if each_obj.collide(p1):
            p1.decrease_hearts(each_obj.damage)
            each_obj.goto(random.choice(random_x), random.choice(random_y))
            road.see_heart(p1)
