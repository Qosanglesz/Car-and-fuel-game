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
        self.shapesize(stretch_wid=2.5, stretch_len=2.5, outline=None)
        self.speed = 0.1
        self.damage = 1
        self.setheading(270)


class Dog(AvoidObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.color("yellow")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2, outline=None)
        self.speed = 0.3
        self.damage = 2
        self.setheading(270)


class Truck(AvoidObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.color("orange")
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=4, outline=None)
        self.speed = 0.2
        self.damage = 3
        self.setheading(270)
