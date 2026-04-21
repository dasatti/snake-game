from turtle import Turtle
import lib.constants as constants

FONT = ("Courier",16,"normal")

class ScoreCard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True, highest = 0):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.speed(0)
        self.color("black")
        self.hideturtle()
        self.show()

    def show(self):
        self.clear()
        self.penup()
        self.goto(0, (constants.SCREEN_HEIGHT / 2) * 1 - 40)
        self.write(f"Score: {self.score}", align="center", font=FONT)
        

    def reset_score(self):
        self.score = 0
        self.update_screen()

    def add_score(self):
        self.score += 1
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.show()

