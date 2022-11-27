from Gameobject import GameObject


class Car(GameObject):
    def __init__(self, shape, color, position):
        # Basic property of object in this game that inheritance form GameObject
        super().__init__(shape, color, position)
        # Additional property for car.
        self.hearts = 5
        self.speed = 25
        self.score = 0
        self.shapesize(stretch_wid=1, stretch_len=1, outline=None)

    # Method for control
    def move(self):
        self.forward(0)

    def control_right(self):
        self.setx(self.xcor() + self.speed)

    def control_left(self):
        self.setx(self.xcor() - self.speed)

    def increase_score(self):
        self.score = self.score + 1

    def decrease_hearts(self, damage):
        self.hearts = self.score - damage
