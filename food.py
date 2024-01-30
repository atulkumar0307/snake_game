from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        x_axis = random.randint(-180, 180)
        y_axis = random.randint(-180, 180)
        self.goto(x_axis, y_axis)
