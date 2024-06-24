from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")
PEN = "white"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor(PEN)
        self.hideturtle()
        self.penup()
        self.setpos(0, 260)
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.setpos(0, 18)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
        self.setpos(0, -18)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
