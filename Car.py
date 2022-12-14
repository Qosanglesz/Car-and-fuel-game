from Gameobject import GameObject


class Car(GameObject):
    def __init__(self, shape="square", color="red", position=(0, -250)):
        # Basic property of object in this game that inheritance form GameObject
        super().__init__(shape, color, position)
        # Additional property for car.
        self.hearts = 5
        self.speed = 30
        self.score = 0
        self.shapesize(stretch_wid=2, stretch_len=1, outline=None)

    # Method for control
    def control_right(self):
        self.setx(self.xcor() + self.speed)
        if self.xcor() > 200:
            self.setx(180)

    def control_left(self):
        self.setx(self.xcor() - self.speed)
        if self.xcor() < -200:
            self.setx(-180)

    # Method for add score
    def increase_score(self):
        self.score = self.score + 1

    # Method for minus heart
    def decrease_hearts(self, damage):
        self.hearts = self.hearts - damage
        if self.hearts < 0:
            self.hearts = 0
