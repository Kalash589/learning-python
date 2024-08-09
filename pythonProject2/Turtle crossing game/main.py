from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import Carmanager
import time




screen=Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.tracer()

scoreboard=Scoreboard()
player=Player()
car_manager=Carmanager()



screen.listen()
screen.onkey(player.move,"Up")



game_on=True
while game_on:
    time.sleep(0.01)
    screen.update()

    car_manager.create_car()

    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_on=False
            scoreboard.game_over()

    if player.is_at_finishline():
        player.goto_startline()
        car_manager.level_up()
        scoreboard.levels()



screen.exitonclick()