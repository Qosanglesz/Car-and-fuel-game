from screen import Screen
from road import Road
from Car import Car
from Fuel import Fuel
import turtle
import random

stage = Screen()
road = Road(400, 900)
stage.init_screen()
road.make()

p1 = Car("circle", "red", position=(0, -400))
fuel = Fuel("square", "green", (0, 800))


road.see_status(p1)
turtle.onkey(p1.control_right, 'd')
turtle.onkey(p1.control_left, 'a')
turtle.listen()

while True:
    turtle.update()
    p1.move()
    fuel.move()
    if fuel.collide(p1):
        p1.increase_score()
        fuel.goto(360, 700)
        road.see_status(p1)


