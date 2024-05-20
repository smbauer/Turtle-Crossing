from turtle import Turtle
import random


COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self) -> None:
        """create a new car object and append it to the list of cars"""
        new_car = Turtle("square")
        new_car.color(random.choice(COLOURS))
        new_car.penup()
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        start_y = random.randint(-250, 250)
        new_car.goto(300, start_y)
        new_car.setheading(180)
        self.cars.append(new_car)


    def move_cars(self) -> None:
        """move each car forward at the current speed/move distance"""
        for car in self.cars:
            if car.xcor() >= -320:
                car.forward(self.car_speed)


    def increase_speed(self) -> None:
        """increase the speed of the cars by the move increment value"""
        self.car_speed += MOVE_INCREMENT
        