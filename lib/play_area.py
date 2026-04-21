from turtle import Turtle
import lib.constants as constants



class PlayArea(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("black")
        self.shape("square")
        self.fillcolor("black")
        self.speed(6)
        self.hideturtle()

    def draw(self):
        self.penup()
        self.goto(constants.PA_TOP_LEFT)
        self.pendown()
        self.begin_fill()
        self.goto(constants.PA_BOTTOM_LEFT)
        self.goto(constants.PA_BOTTOM_RIGHT)
        self.goto(constants.PA_TOP_RIGHT)
        self.goto(constants.PA_TOP_LEFT)
        self.end_fill()
