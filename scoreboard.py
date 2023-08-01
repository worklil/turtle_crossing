from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")
FONT2 = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-200, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT2)

    def level_up(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

