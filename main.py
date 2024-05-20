from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
import random


# create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# create turtle, car manager (cars), and scoreboard
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# move turtle with up key
screen.onkeypress(fun=player.move, key="Up")
screen.onkeypress(fun=screen.bye, key="space")
screen.listen()

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    # create car at random interval
    rand_chance = random.randint(1, 6)
    if rand_chance == 1:
        car_manager.create_car()

    # detect player reaching top of screen
    if player.crossed():
        # increment level when turtle reaches top of screen
        scoreboard.increment_level()
        # reset player/cars and increase car speed
        player.reset_player()
        car_manager.increase_speed()

    # detect turtle collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            # end game on car collision
            game_on = False
            scoreboard.game_over()

    car_manager.move_cars()

screen.exitonclick()
