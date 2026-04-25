from turtle import Turtle
import lib.constants as constants

FONT = ("Courier",16,"normal")

class Highest(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True,):
        super().__init__(shape, undobuffersize, visible)
        self.highest = self.load()
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
            self.save()

    def load(self):
        try:
            with open("score") as f:
                return int(f.read())
        except:
            return 0

    def save(self):
        try:
            with open("score","w") as f:
                f.write(f"{self.highest}")
        except:
            pass
