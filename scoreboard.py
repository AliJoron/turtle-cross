from turtle import Turtle
FONT = ("Courier", 11, "bold")
OVER = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-260, 270)
        self.hideturtle()
        self.write(f"Level: {self.score}", align='center', font=FONT)
        self.color("black")

    def finish(self):

        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align='center', font=FONT)

    def game_over(self):

        self.goto(0,0)
        self.write("Game Over", align='center', font=OVER)



