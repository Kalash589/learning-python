from turtle import Turtle

STARTING_POSITION=(0,-280)
MOVE_DIST=10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.shapesize(1,1)
        self.goto(0 , -280)

    def move(self):
        self.goto(0,self.ycor() + 10)


    def goto_startline(self):
        self.goto(STARTING_POSITION)

    def is_at_finishline(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

