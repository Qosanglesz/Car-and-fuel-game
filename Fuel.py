from Gameobject import GameObject


class Fuel(GameObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5, outline=None)
        self.speed = 0.5
        self.setheading(270)

    # method to set fuel go down(-y direction)
    def move(self):
        self.sety(self.ycor() - self.speed)
