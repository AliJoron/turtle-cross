import time
from turtle import Screen
import car_manager
import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


car = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
turtle = Player()
score = Scoreboard()
screen.onkeypress(turtle.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create()
    car.move()

    for cars in car.all_cars:
        if cars.distance(turtle) < 20:
            game_is_on = False
            score.game_over()
    if turtle.ycor() > player.FINISH_LINE_Y:
        turtle.goto(player.STARTING_POSITION)
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
        score.finish()

screen.exitonclick()