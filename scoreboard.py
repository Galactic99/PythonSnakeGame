
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
        with open("data.txt") as file:
            self.high_score = file.read()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", move=False, align="center", font=("Arial", 12, "normal"))

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
            with open("data.txt") as data:
                self.high_score = data.read()
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", move=False, align="center", font=("Arial", 25, "normal"))



    def increase_score(self):
        self.score += 1
        self.update_score()

