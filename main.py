from turtle import Screen
from game_options import Settings
from pong import Pong
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
game = Settings()
pong = Pong()
ball = Ball()
scoreboard = ScoreBoard()
game.key_movement(pong)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    if ball.check_hit_wall():
        ball.bounce_x()
    elif pong.check_hit_paddle(ball):
        ball.bounce_y()
    elif ball.check_right_paddle_miss():
        ball.reset_position()
        scoreboard.point_left_paddle()
    elif ball.check_left_paddle_miss():
        ball.reset_position()
        scoreboard.point_right_paddle()
    if scoreboard.there_is_a_winner():
        game_is_on = False

screen.exitonclick()
