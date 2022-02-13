from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.forward(position)


    def go_up(self):
        y_core = self.ycor() + 20
        self.goto(self.xcor(), y_core)

    def go_down(self):
        y_core = self.ycor() - 20
        self.goto(self.xcor(), y_core)
