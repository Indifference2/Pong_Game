from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def create_ball(self):
        """Model ball shape, color and size"""
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)

    def move_ball(self):
        new_y = self.ycor() + self.x_move
        new_x = self.xcor() + self.y_move
        self.goto(new_x, new_y)

    def check_hit_wall(self):
        if self.ycor() > 290 or self.ycor() < -290:
            return True

    def check_right_paddle_miss(self):
        if self.xcor() > 390:
            return True

    def check_left_paddle_miss(self):
        if self.xcor() < -390:
            return True

    def bounce_x(self):
        """Decrease ball in the axis X and increase his speed"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        """Decrease ball in the axis Y and increase his speed"""
        self.y_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset ball to position (0, 0) and his speed each time a player score"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_y()
