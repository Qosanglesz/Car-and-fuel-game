from turtle import Turtle


class Screen:
    def init_screen(self):
        self.display = Turtle()
        self.display.screen.setup(600, 900)
        self.display.hideturtle()
        self.display.penup()
        self.display.forward(0)
        self.display.speed(0)
        self.display.screen.title("Car and fuel game")
