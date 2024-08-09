from turtle import Turtle

FONT=("Courier",24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.level=1
        self.update()

    def update(self):
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER" , align="Centre" , font=FONT)

    def levels(self):
        self.clear()
        self.level += 1
        self.update()