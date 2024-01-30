from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]    # making constant so that we can use them anywhere in the program and their value won't change.
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):     # initializer/ constructor or class should have.
        self.segments = []      # making a list so that we can perform operation on this list.
        self.create_snake()     # calling the method create_snake in constructor.
        self.head = self.segments[0]    # assigning the segment[0] to head so that we don't have to use segment[0] all time.

    def create_snake(self):     # method.
        for starting_position in POSITIONS:  # making the body of snake with 3 turtle of square shape.
            self.add_segment(starting_position)

    def add_segment(self, starting_position):
        new_turtle = Turtle("square")
        new_turtle.color("green")
        new_turtle.penup()
        new_turtle.goto(starting_position)
        self.segments.append(new_turtle)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extent_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # making a reverse range so that we can move the last segment to the last 2nd segment position.
            x_seg = self.segments[seg_num - 1].xcor()  # finding the x coordinate of last 2nd segment.
            y_seg = self.segments[seg_num - 1].ycor()  # finding the y coordinate of last 2nd segment.
            self.segments[seg_num].goto(x_seg, y_seg)  # assigning the location of 2nd last segment to last segment.
        self.head.forward(MOVE_DISTANCE)  # making 1st segment move so that remaining can follow its path as previously mentioned.

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
