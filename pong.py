from turtle import Turtle

POS_PLAYERS = [(-350, 0), (350, 0)]


class Pong:
    def __init__(self):
        self.segments = []
        self.create_players()
        self.left_paddle = self.segments[0]
        self.right_paddle = self.segments[1]

    def create_players(self):
        for position in POS_PLAYERS:
            self.player(position)

    def player(self, POSITION):
        """Model paddle, shape, size and position"""
        paddle = Turtle("square")
        paddle.turtlesize(5, 1)
        paddle.color("white")
        paddle.penup()
        paddle.setposition(POSITION)
        self.segments.append(paddle)

    def player1_up(self):
        new_y = self.left_paddle.ycor() + 20
        self.left_paddle.goto(self.left_paddle.xcor(), new_y)

    def player1_down(self):
        new_y = self.left_paddle.ycor() + -20
        self.left_paddle.goto(self.left_paddle.xcor(), new_y)

    def player2_up(self):
        new_y = self.right_paddle.ycor() + 20
        self.right_paddle.goto(self.right_paddle.xcor(), new_y)

    def player2_down(self):
        new_y = self.right_paddle.ycor() + -20
        self.right_paddle.goto(self.right_paddle.xcor(), new_y)

    def check_hit_paddle(self, Ball):
        if ((self.right_paddle.distance(Ball) < 45 and self.right_paddle.xcor() > 320)
                or (self.left_paddle.distance(Ball) < 45 and self.left_paddle.xcor() < -320)):
            return True
