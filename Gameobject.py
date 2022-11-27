import turtle


class GameObject(turtle.Turtle):
    def __init__(self, shape, color, position):
        turtle.Turtle.__init__(self, shape)
        self.color(color)
        self.goto(position)
        self.speed(0)
