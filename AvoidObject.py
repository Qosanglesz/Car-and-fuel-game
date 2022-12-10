from Gameobject import GameObject


# inheritance from Game object this class is super class of avoid object.
class AvoidObject(GameObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.speed = 0
        self.setheading(270)

    def move(self):
        self.sety(self.ycor() - self.speed)

# Subclass of Superclass avoid object will have different speed and damages


class Hole(AvoidObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.shapesize(stretch_wid=2.5, stretch_len=2.5, outline=None)
        self.speed = 0.1
        self.damage = 1


class Dog(AvoidObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.shapesize(stretch_wid=1, stretch_len=2, outline=None)
        self.speed = 0.3
        self.damage = 2


class Truck(AvoidObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.shapesize(stretch_wid=2, stretch_len=4, outline=None)
        self.speed = 0.2
        self.damage = 3
