from turtle import Turtle
import random


COLORS=["red","yellow","orange","pink","blue"]
STARTING_MOVE_DIST=5
MOVE_INCREAMENT=10

class Carmanager():

    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DIST

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y_pos=random.randint(-250,250)
            new_car.goto(300,y_pos)
            self.all_cars.append(new_car)

    def  move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREAMENT
