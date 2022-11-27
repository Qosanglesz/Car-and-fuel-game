from Gameobject import GameObject


class Fuel(GameObject):
    def __init__(self, shape, color, position):
        super().__init__(shape, color, position)
        self.shape("square")
        self.color("green")
        self.shape("circle")
        self.shapesize(stretch_wid=2, stretch_len=2, outline=None)
        self.speed = 5
        self.setheading(270)

    def move(self):
        self.sety(self.ycor() - self.speed)

