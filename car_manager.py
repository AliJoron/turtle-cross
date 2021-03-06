import time
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):

        self.all_cars = []

    def create(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle()
            y = random.randint(-250, 250)
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    def move(self):

        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
