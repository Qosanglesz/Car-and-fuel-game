import turtle


class Road:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pen = turtle.Turtle()
        self.pencil = turtle.Turtle()

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
        self.pen.setposition(-290, 250)
        self.pen.write(text_score, font=("Arial", 16, "normal"))

    def see_heart(self, obj):
        self.pencil.undo()
        text_heart = f"Heart: {obj.hearts}"
        self.pencil.speed(0)
        self.pencil.penup()
        self.pencil.hideturtle()
        self.pencil.setposition(210, 250)
        self.pencil.write(text_heart, font=("Arial", 16, "normal"))
