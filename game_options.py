from turtle import Turtle, Screen


class Settings:
    def __init__(self):
        self.score = Turtle()
        self.screen = Screen()
        self.screen_options()

    def screen_options(self):
        """Create the screen and title"""
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong Game")
        self.screen.tracer(0)

    def key_movement(self, Pong):
        """KEY BINDING PLAYERS"""
        self.screen.listen()
        self.screen.onkey(Pong.player1_up, "w")
        self.screen.onkey(Pong.player1_down, "s")
        self.screen.onkey(Pong.player2_up, "Up")
        self.screen.onkey(Pong.player2_down, "Down")


