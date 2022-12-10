import turtle

# Every object in game use this class to Superclass


class GameObject(turtle.Turtle):
    def __init__(self, shape, color, position):
        turtle.Turtle.__init__(self, shape=shape)
        self.penup()
        self.color(color)
        self.speed(0)
        self.goto(position)

    def collide(self, other):
        if (other.xcor() - 30 <= self.xcor() <= other.xcor() + 30 and
                other.ycor() - 30 <= self.ycor() <= other.ycor() + 30):
            return True

        return False
