from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 60, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.update_score()

    def set_middleline(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.pendown()
        for _ in range(30):
            self.width(10)
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()

    def score_r(self):
        self.score_right +=1
        self.update_score()

    def score_l(self):
        self.score_left +=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(f"{self.score_left}", False, align="center", font=FONT),
        self.goto(x=100, y=200)
        self.write(f"{self.score_right}", False, align="center", font=FONT)
