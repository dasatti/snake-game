from turtle import Turtle
import lib.constants as constants


class Snake:
    def __init__(self, name="snake-1"):
        self.size = 3
        self.initial_x = 0
        self.positions = []
        self.segments = []
        self.alive = True
        self.head = None
        self.score = 0
        self.name = name
        self.speed = 0

        for X in range(self.size):
            self.initial_x -= 20
            self.positions.append((self.initial_x,0))


    def spawn(self):
        for p in self.positions:
            t = Turtle(shape="square")
            t.speed(self.speed )
            t.color("green")
            t.penup()
            t.goto(p)
            self.segments.append(t)
            self.direction = 'left'
        self.head = self.segments[0]

    def grow(self):
        tail_segment = self.segments[-1]
        t = Turtle(shape="square")
        t.hideturtle()
        t.speed(0)
        t.color("green")
        t.penup()
        t.setheading(tail_segment.heading())
        t.goto(tail_segment.pos())
        t.backward(constants.MOVE_DISTANCE)
        t.speed(self.speed )
        # t.screen.update()
        t.showturtle()
        self.segments.append(t)

    def eat(self):
        self.score += 1
        self.grow()

    def turn_right(self):
        if self.head.heading() != constants.LEFT:
            self.head.setheading(constants.RIGHT)
    
    def turn_left(self):
        if self.head.heading() != constants.RIGHT:
            self.head.setheading(constants.LEFT)

    def turn_up(self):
        if self.head.heading() != constants.DOWN:
            self.head.setheading(constants.UP)
        
    def turn_down(self):
        if self.head.heading() != constants.UP:
            self.head.setheading(constants.DOWN)

    def stop(self):
        self.move = False

    def is_self_collide(self):
        for s in self.segments[2:]:
            if s.distance(self.head) < 10:
                return True
        return False
    
    def die(self):
        self.alive = False
        for t in self.segments:
            t.hideturtle()
            t.clear()
        self.segments.clear()

    def move(self):
        if self.alive:
            for i in range(len(self.segments)-1,0,-1):
                self.segments[i].goto(self.segments[i - 1].pos())
            self.head.forward(constants.MOVE_DISTANCE)




