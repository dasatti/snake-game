from turtle import Screen
from lib.snake import Snake
from lib.food import Food
from lib.scorecard import ScoreCard
from lib.game_over import GameOver
from lib.play_area import PlayArea
from lib.total_games import TotalGames
from lib.footer import Footer
from lib.highest import Highest
import lib.constants as constants
import time


class SnakeGame():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
        self.screen.title("Snake Game")
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        self.snake = None
        self.food = None
        self.scorecard = ScoreCard()
        self.play_area = None
        self.footer = None
        self.highest = Highest()
        self.total_games = TotalGames()
        self.play_game = False
        self.dead = False

        self.screen_x_start = constants.PA_TOP_LEFT[0]
        self.screen_x_end = constants.PA_TOP_RIGHT[0]
        self.screen_y_start = constants.PA_BOTTOM_LEFT[1]
        self.screen_y_end= constants.PA_TOP_LEFT[1]

    def out_of_screen(self):
        head = self.snake.head
        if head.xcor() > self.screen_x_end or head.xcor() < self.screen_x_start:
            return True
        if head.ycor() > self.screen_y_end or head.ycor() < self.screen_y_start:
            return True
        return False

    def game_over(self):
        self.dead = True
        self.score = self.scorecard.score
        self.highest.set_new_high(self.score)
        self.snake.die()
        self.food.hideturtle()
        del self.snake
        del self.food
        self.go = GameOver()
        self.go.show()

    def exit_game(self):
        self.play_game = False
        self.screen.bye()

    def new_game(self):
        self.dead = False
        self.play_game = False
        self.screen.clear()
        # screen.bgcolor("black")
        self.snake = Snake()
        self.food = Food()
        self.play_area = PlayArea()
        # scorecard = ScoreCard(highest=highest)
        self.scorecard.reset_score()
        self.highest.show()
        self.total_games.add_game()
        
        self.footer = Footer()
        self.play_area.draw()
        self.snake.spawn()
        print("New Game Play")
        print(f"Playing new game with snake {self.snake.name}")
        self.screen.update()
        self.screen.listen()
        self.screen.onkey(self.play,"space")
        self.screen.onkey(self.new_game,"n")
        self.screen.onkey(self.snake.turn_left,"a")
        self.screen.onkey(self.snake.turn_left,"Left")
        self.screen.onkey(self.snake.turn_right,"d")
        self.screen.onkey(self.snake.turn_right,"Right")
        self.screen.onkey(self.snake.turn_up,"w")
        self.screen.onkey(self.snake.turn_up,"Up")
        self.screen.onkey(self.snake.turn_down,"s")
        self.screen.onkey(self.snake.turn_down,"Down")
        self.screen.onkey(self.snake.grow,"g")
        self.screen.onkey(self.exit_game,"x")
        # self.screen.exitonclick()
        self.screen.mainloop()

    

    def play(self):
        self.play_game =  not self.play_game
        if not self.play_game:
            self.food.hideturtle()
        else:
            self.food.showturtle()
        while self.play_game and not self.dead:
            self.snake.move()
            if self.snake.head.distance(self.food) < 15:
                self.food.change_position()
                self.snake.eat()
                self.scorecard.add_score()
            if self.out_of_screen():
                self.game_over()
            elif self.snake.is_self_collide():
                self.game_over()
            
            time.sleep(0.02)
            self.screen.update()



def main():
    snake_game = SnakeGame()
    snake_game.new_game()

if __name__ == "__main__":
    main()


