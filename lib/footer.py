from turtle import Turtle
import lib.constants as constants
FONT = ("Courier",10,"normal")

class Footer(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.goto((constants.PA_BOTTOM_LEFT[0] + 60,constants.PA_BOTTOM_LEFT[1] - 30))
        self.setheading(180)
        self.forward(150)
        self.setheading(0)
        self.forward(100)
        self.pendown()
        self.write("Pause : [space]", font=FONT, align="left")
        self.penup()
        self.goto((0, constants.PA_BOTTOM_LEFT[1] - 30))
        self.write("New Game: [n]", font=FONT, align="center")
        self.goto((constants.PA_BOTTOM_RIGHT[0], constants.PA_BOTTOM_LEFT[1] - 30))
        self.write("Quit: [x]", font=FONT, align="right")