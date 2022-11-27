import turtle


class Road:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pen = turtle.Turtle()

    def make(self):
        self.pen.penup()
        self.pen.speed(0)
        self.pen.setposition(-200, -450)
        self.pen.pensize(3)
        self.pen.pendown()
        for i in range(2):
            self.pen.forward(self.width)
            self.pen.left(90)
            self.pen.forward(self.height)
            self.pen.left(90)

    def see_status(self, obj):
        self.pen.undo()
        text_score = f"Score:{obj.score}"
        text_heart = f"Heart: {obj.hearts}"
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.setposition(210, 400)
        self.pen.write(text_heart, font=("Arial", 16, "normal"))
        self.pen.setposition(-290, 400)
        self.pen.write(text_score, font=("Arial", 16, "normal"))
