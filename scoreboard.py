
from turtle import Turtle, Screen

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        self.update_score()


    def update_score(self):
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align="center", font=("Arial", 25, "normal"))



    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

