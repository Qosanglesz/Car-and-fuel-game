import Gameobject


class Car(Gameobject):
    def __init__(self, shape, color, position):
        # Basic property of object in this game that inheritance form GameObject
        super().__init__(shape, color, position)
        # Additional property for car.
        self.hearts = 5
        self.speed = 5
        self.score = 0
        self.shapesize(stretch_wid=5, stretch_len=5, outline=None)

    # Method for control
    def right(self):
        self.setx(self.xcor() + self.speed)

    def left(self):
        self.setx(self.xcor() - self.speed)
