from turtle import Turtle
import lib.constants as constants

FONT = ("Courier",16,"normal")

class TotalGames(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.total_games = -1
        self.speed(0)
        self.color("black")
        self.hideturtle()
        self.show()

    def show(self):
        self.clear()
        self.penup()
        self.goto((constants.SCREEN_HEIGHT / 2) * 1 - 10 , (constants.SCREEN_HEIGHT / 2) * 1 - 40)
        self.write(f"Games: {self.total_games}", align="right", font=FONT)


    def add_game(self):
        self.total_games += 1
        self.show()
