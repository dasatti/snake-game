from turtle import Turtle
import random
import lib.constants as constants


class Food(Turtle):
    def __init__(self, shape = "circle", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("yellow")
        self.speed(0)
        self.penup()
        self.start_x = int(constants.SCREEN_WIDTH / 2) * -1 + constants.PA_MARGIN_X
        self.end_x = int(constants.SCREEN_WIDTH / 2) * 1 - constants.PA_MARGIN_X
        self.start_y = int(constants.SCREEN_HEIGHT / 2) * -1 + constants.PA_MARGIN_Y
        self.end_y = int(constants.SCREEN_HEIGHT / 2) * 1 - constants.PA_MARGIN_Y
        self.change_position()

    def change_position(self):
        random_x = random.randint(self.start_x + 5, self.end_x - 5)
        random_y = random.randint(self.start_y + 5, self.end_y - 5)
        self.goto(float(random_x), float(random_y))


