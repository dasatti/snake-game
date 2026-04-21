from turtle import Turtle
import lib.constants as constants

FONT = ("Courier",16,"normal")

class Highest(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True, highest = 0):
        super().__init__(shape, undobuffersize, visible)
        self.highest = highest
        self.color("black")
        self.show()

    
    def show(self):
        self.clear()
        self.penup()
        self.goto((constants.SCREEN_HEIGHT / 2) * -1 + 10 , (constants.SCREEN_HEIGHT / 2) * 1 - 40)
        self.write(f"High: {self.highest}", align="left", font=FONT)

        
    def set_new_high(self, highest):
        if self.highest < highest:
            self.highest = highest
            self.show()
