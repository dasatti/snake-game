from turtle import Turtle
import lib.constants as constants

ALIGNMENT = "center"
FONT = ("Courier",20,"normal")
FONT_2 = ("Courier",12,"normal")

class GameOver(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.hideturtle()
        self.penup()
        # self.backward(4)
        # self.goto(-20, (constants.SCREEN_HEIGHT / 2) * 1 - 40)
        # self.show()

    def show(self):
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        self.setpos((0, -30))
        self.write("Press (n) to start new game", align=ALIGNMENT, font=FONT_2)

    def hide(self):
        self.clear()
