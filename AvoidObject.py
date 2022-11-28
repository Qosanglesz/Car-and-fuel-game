from Gameobject import GameObject


class AvoidObject(GameObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.speed = 0

    def move(self):
        self.sety(self.ycor() - self.speed)


class Hole(AvoidObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.color("black")
        self.shape("circle")
        self.shapesize(stretch_wid=2, stretch_len=2, outline=None)
        self.speed = 0.1
        self.damage = 1
        self.setheading(270)


class Dog(AvoidObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.color("yellow")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=1, outline=None)
        self.speed = 0.5
        self.damage = 2
        self.setheading(270)


class Truck(AvoidObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.color("red")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3, outline=None)
        self.speed = 0.2
        self.damage = 3
        self.setheading(270)
