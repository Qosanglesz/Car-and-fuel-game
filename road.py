import turtle
from collections import Counter


class Road:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pen = turtle.Turtle()
        self.pencil = turtle.Turtle()
        self.over = turtle.Turtle()
        self.over.hideturtle()

    # Drawing boarder road in screen
    def make(self):
        self.pen.penup()
        self.pen.speed(0)
        self.pen.setposition(-200, -450)
        self.pen.pensize(3)
        self.pen.pendown()
        self.pen.color("white")
        for i in range(2):
            self.pen.forward(self.width)
            self.pen.left(90)
            self.pen.forward(self.height)
            self.pen.left(90)

    # GAME OVER SCREEN
    def game_over(self, obj):
        self.over.penup()
        self.over.speed(0)
        self.over.goto(0, 50)
        self.over.color("Red")
        self.over.write("WASTED", align="center", font=("Tahoma", 20, "bold"))
        self.over.goto(0, 30)
        self.over.color("black")
        self.over.write(f"current score: {obj.score}", align="center", font=("Tahoma", 18, "bold"))

    # Show status method (Score)
    def see_score(self, obj):
        self.pen.undo()
        text_score = f"Score:{obj.score}"
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.setposition(-290, 250)
        self.pen.write(text_score, font=("Arial", 16, "normal"))

    # Show status method (Hearts)
    def see_heart(self, obj):
        self.pencil.undo()
        text_heart = f"Heart: {obj.hearts}"
        self.pencil.speed(0)
        self.pencil.penup()
        self.pencil.hideturtle()
        self.pencil.setposition(210, 250)
        self.pencil.color("white")
        self.pencil.write(text_heart, font=("Arial", 16, "normal"))

    # Method to show score board of top 3 of player from database XD
    def score_board(self, data_dict):
        self.over.goto(0, self.over.ycor() - 50)
        self.over.color("Red")
        self.over.write("TOP 3 SCORE", align="center", font=("Tahoma", 20, "bold"))
        self.over.goto(0, self.over.ycor() - 25)
        top_3player = dict(Counter(data_dict).most_common(3))
        self.over.color("Black")
        for keys, values in top_3player.items():
            msg = f"{keys:<5}{str(values):>5}"
            self.over.write(msg, align='center', font=("Tahoma", 15, "bold"))
            self.over.goto(0, self.over.ycor()-25)
