from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(f"{self.l_score}", align="center", font=("Courier", 70, "normal"))
        self.goto(100, 180)
        self.write(f"{self.r_score}", align="center", font=("Courier", 70, "normal"))

    def point_left_paddle(self):

        self.l_score += 1
        self.update_scoreboard()

    def point_right_paddle(self):
        self.r_score += 1
        self.update_scoreboard()

    def there_is_a_winner(self):
        if self.l_score == 5:
            self.goto(0, 0)
            self.write("PLAYER 1 WIN", align="center", font=("Courier", 70, "normal"))
            return True
        elif self.r_score == 5:
            self.goto(0, 0)
            self.write("PLAYER 2 WIN", align="center", font=("Courier", 70, "normal"))
            return True
