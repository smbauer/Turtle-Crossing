from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self) -> None:
        """move player forward by specified distance"""
        self.forward(MOVE_DISTANCE)


    def crossed(self) -> bool:
        """return true if player reaches finish line"""
        return self.ycor() >= FINISH_LINE_Y
    

    def reset_player(self) -> None:
        """return the player to the starting position"""
        self.goto(STARTING_POSITION)