from turtle import Turtle


FONT = ("Courier", 24, "normal")
SCOREBOARD_LOCATION = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.refresh_scoreboard()

    
    def refresh_scoreboard(self) -> None:
        """update the scoreboard with the current level at the top of the screen"""
        self.clear()
        self.goto(SCOREBOARD_LOCATION)
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def increment_level(self) -> None:
        """increment the current level"""
        self.level += 1
        self.refresh_scoreboard()


    def game_over(self) -> bool:
        """writes the game over message in the middle of the screen"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
